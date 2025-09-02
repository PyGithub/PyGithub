#!/bin/bash

set -euo pipefail

index=openapi.index
scripts_path="$(cd "$(dirname "$0")"; pwd)"
source_path="$scripts_path/../github"
openapi="$scripts_path/openapi.py"
sort_class="$scripts_path/sort_class.py"
prepare_for_update_assertions="$scripts_path/prepare-for-update-assertions.py"
update_assertions="$scripts_path/update-assertions.sh"
spec=api.github.com.2022-11-28.json
python="$(which python3)"
pytest_bin="$(which pytest)"
pre_commit_bin="$(which pre-commit)"
mypy_bin="$(which mypy)"
git=git
jq=jq

RED='\033[1;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
GREY='\033[0;37m'
NOCOLOR='\033[0m'

# check there are no git changes
if ! "$git" diff --quiet; then
  echo "There are pending git changes, cannot run this script"
  exit 1
fi

# check for some options
create_classes=
single_branch=
branch_prefix="openapi/update"
while [ $# -ge 1 ]; do
  if [ "$1" == "--create-classes" ]; then
    create_classes="true"
    shift 1
  elif [ $# -ge 2  ] && [ "$1" == "--branch" ]; then
    single_branch="$2"
    shift 2
  elif [ $# -ge 2  ] && [ "$1" == "--branch-prefix" ]; then
    branch_prefix="$2"
    shift 2
  else
    break
  fi
done

# update index
echo -n "Updating index ($index)" | tee >(cat 1>&2)
"$python" "$openapi" index "$source_path" "$spec" "$index" | while read -r line; do echo -n .; done
echo | tee >(cat 1>&2)

# get all GithubObject classes
if [ $# -ge 1 ]; then
  github_classes=("$@")
else
  read -r -a github_classes <<< "$("$jq" -r '.indices.class_to_descendants.GithubObject | @tsv' < "$index")"
fi

# skip abstract classes
concrete_github_classes=()
for class in "${github_classes[@]}"; do
  if [[ "$("$jq" ".classes.$class.bases | index(\"ABC\")" < "$index")" == "null" ]]; then
    concrete_github_classes+=($class)
  fi
done
github_classes=("${concrete_github_classes[@]}")
max_class_name_length=$(for class_name in "${github_classes[@]}"; do echo -n "$class_name" | wc -c; done | sort -rn | head -n1)
spaces="$(head -c "$max_class_name_length" < /dev/zero | tr '\0' ' ')"

commit() {
  do_lint=true
  if [ $# -gt 0 ] && [ "$1" == "--no-linting" ]; then
    do_lint=false
    shift
  fi
  force_lint=false
  if [ $# -gt 0 ] && [ "$1" == "--force-linting" ]; then
    force_lint=true
    shift
  fi
  if [ $# -lt 1 ]; then
    echo "Cannot commit without message"
    exit 1
  fi
  message="$1"
  shift

  # skip if there are no changes, unless linting is forced
  if [[ "$force_lint" != "true" ]] && "$git" diff --quiet; then return 0; fi

  # run linting
  if [[ "$do_lint" == "true" ]]; then
    "$mypy_bin" github tests 1>&2
    "$pre_commit_bin" run --all-files --show-diff-on-failure 1>&2 || true
  fi

  # skip if there are no changes after linting
  if "$git" diff --exit-code 1>&2; then return 0; fi

  # commit
  "$git" commit -a -m "$message" "$@" 1>&2
  echo 1>&2
  return 255
}

# apply schemas on all classes iteratively, until no more schemas could be applied
last_schemas=$("$jq" ".indices.schema_to_classes | length" < "$index")
echo -n "Adding schemas to ${#github_classes[@]} classes:" | tee >(cat 1>&2)
while true; do
  "$python" "$openapi" suggest schemas --add "$spec" "$index" "${github_classes[@]}" 1>&2
  "$python" "$openapi" index "$source_path" "$spec" "$index" | while read -r line; do echo -n .; done
  now_schemas=$("$jq" ".indices.schema_to_classes | length" < "$index")
  if [ "$now_schemas" -eq "$last_schemas" ]; then break; fi
  echo -n "$now_schemas" | tee >(cat 1>&2)
  last_schemas="$now_schemas"
done
echo | tee >(cat 1>&2)
commit "Added schemas to classes" || true

unchanged() {
  echo -n -e " [${GREEN}$1${NOCOLOR}]" | tee >(cat 1>&2)
  echo 1>&2
}

changed() {
  if [ $? -eq 255 ]; then
    echo -n -e " [${YELLOW}$1${NOCOLOR}]" | tee >(cat 1>&2)
    echo 1>&2
  else
    failed "$2"
  fi
}

skip() {
  echo -n -e " [${GREY}$1${NOCOLOR}]" | tee >(cat 1>&2);
  echo 1>&2
}

failed() {
  echo -n -e " [${RED}$1${NOCOLOR}]" | tee >(cat 1>&2)
  echo 1>&2
  false
}

update_in_branch() {
  # base branch where the class-specific branch originates from
  base="$1"; shift
  branch=
  if [ $# -gt 1 ]; then
    branch="$1"; shift
    if [ $# -eq 1 ]; then class="class"; else class="classes"; fi
  else
    branch="$branch_prefix-$1"
    class="class"
  fi

  # move to base branch
  "$git" checkout -f "$base" 1>&2

  # switch into class-specific branch
  if [[ $("$git" branch --list "$branch" | sed -E -e "s/^[*]? +//") != "" ]]; then
    "$git" branch -m "$branch" "$branch-$(date +%s)" 1>&2
  fi
  "$git" checkout -b "$branch" 1>&2

  # update class(es)
  update "$class" "$@"

  # remove class-specific branch if there are no changes, restore base branch
  if "$git" diff --quiet "$base"; then
    "$git" branch -m "$branch" "$branch-$(date +%s)" 1>&2
  else
    echo -n -e " ${BLUE}($branch)${NOCOLOR}" | tee >(cat 1>&2)
  fi
  echo

  "$git" checkout "$base" 1>&2
}

update() {
  # class(es) label
  class="$1"; shift
  # classes to update
  classes=("$@")

  # classes with test files
  test_files=()
  classes_with_tests=()
  for github_class in "${classes[@]}"; do
    test_file="tests/$github_class.py"
    if [ -f "$test_file" ]; then
      test_files+=("$test_file")
      classes_with_tests+=("$github_class")
    fi
  done

  # add schemas to class
  for github_class in "${classes[@]}"; do
    ("$python" "$openapi" suggest schemas --add "$spec" "$index" "$github_class" && echo) 1>&2
  done || failed "schemas" || return 0
  commit "Add OpenAPI schemas to $class" && unchanged "schemas" || changed "schemas" "schemas" || return 0

  # update index
  "$python" "$openapi" index "$source_path" "$spec" "$index" 1>&2

  # sort the class
  ("$python" "$sort_class" "$index" "${classes[@]}" && echo) 1>&2 || failed "sort" || return 0
  commit "Sort attributes and methods in $class" && unchanged "sort" || changed "sort" "sort" || return 0

  # apply schemas to class
  ("$python" "$openapi" apply ${create_classes:+--new-schemas create-class} "$source_path" "$spec" "$index" "${classes[@]}" && echo) 1>&2 || failed "$class" || return 0
  if [ -n "$create_classes" ]; then git add github/; fi
  commit "Updated $class according to API spec" && unchanged "$class" || changed "$class" "$class" || return 0

  # apply schemas to test class
  if [ ${#classes_with_tests[@]} -gt 0 ]; then
    ("$python" "$openapi" apply --tests ${create_classes:+--new-schemas create-class} "$source_path" "$spec" "$index" "${classes_with_tests[@]}" && if [ -n "$create_classes" ]; then git add tests/; fi; echo) 1>&2 || failed "tests" || return 0
  fi
  # do not perform linting as part of the commit as this step
  # introduces imports that might be needed by assertions
  # committing assertions will run linting to clean this up
  commit --no-linting "Updated test $class according to API spec" && unchanged "tests" || changed "tests" "tests" || return 0

  # fix test assertions
  if [[ "$(git log -1 --pretty=%B HEAD)" == "Updated test $class according to API spec"* ]]; then
    for test_file in "${test_files[@]}"; do
      (
        # reconstruct long lines
        "$python" "$prepare_for_update_assertions" "$test_file" testAttributes 1>&2 || true
        # update assertions
        "$update_assertions" "$test_file" testAttributes 2>&1 | while read line; do echo "$test_file: $line"; done 1>&2 || true
      ) &
      echo 1>&2
    done
    wait
  fi
  commit --force-linting "Updated test assertions" && unchanged "assertions" || changed "assertions" "assertions" || return 0

  # run tests
  if [ ${#test_files[@]} -gt 0 ]; then
    code=0
    "$pytest_bin" "${test_files[@]}" -k testAttributes 1>&2 || code=$?
    if [ $code -eq 5 ]; then
      skip "pass"
    elif [ $code -eq 0 ]; then
      unchanged "pass"
    else
      failed "pass" || true
    fi
  else
    skip "pass"
  fi
}

# memorize current base commit
base=$("$git" rev-parse --abbrev-ref HEAD)

# update index
echo -n "Updating index ($index)" | tee >(cat 1>&2)
"$python" "$openapi" index "$source_path" "$spec" "$index" | while read -r line; do echo -n .; done
echo | tee >(cat 1>&2)

# update all classes
echo "Updating ${#github_classes[@]} classes:" | tee >(cat 1>&2)
if [[ -n "$single_branch" ]]; then
  echo -n "${#github_classes[@]} PyGithub classes:" | tee >(cat 1>&2)
  update_in_branch "$base" "$single_branch" "${github_classes[@]}"
else
  for github_class in "${github_classes[@]}"; do
    echo -n "${spaces:${#github_class}}$github_class:" | tee >(cat 1>&2)
    update_in_branch "$base" "$github_class"
  done
fi

# recreate index
echo -n "Updating index ($index)" | tee >(cat 1>&2)
"$python" "$openapi" index "$source_path" "$spec" "$index" | while read -r line; do echo -n .; done
echo | tee >(cat 1>&2)
