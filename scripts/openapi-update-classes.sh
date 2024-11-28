#!/bin/bash

set -euo pipefail

index=openapi.index
scripts_path="$(cd "$(dirname "$0")"; pwd)"
source_path="$scripts_path/../github"
openapi="$scripts_path/openapi.py"
sort_class="$scripts_path/sort_class.py"
pre_commit_conf="$scripts_path/openapi-update-classes.pre-commit-config.yaml"
update_assertions="./$scripts_path/update-assertions.sh"
spec=api.github.com.2022-11-28.json
python_bin="$scripts_path/../../venv-PyGithub/bin"
python="$python_bin/python3"
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
single_branch=
if [ $# -ge 2 ]; then
  if [ "$1" == "--branch" ]; then
    single_branch="$2"
    shift 2
  fi
fi

# get all GithubObject classes
if [ $# -ge 1 ]; then
  github_classes="$@"
else
  github_classes="$("$jq" -r '.indices.class_to_descendants.GithubObject | @tsv' < "$index")"
fi

# skip abstract classes
github_classes="$(for class in $github_classes; do
  if [[ "$($jq ".classes.$class.bases | index(\"ABC\")" < "$index")" == "null" ]]; then
    echo $class
  fi
done)"
max_class_name_length=$(for class_name in $github_classes; do echo -n "$class_name" | wc -c; done | sort -rn | head -n1)
spaces="$(head -c "$max_class_name_length" < /dev/zero | tr '\0' ' ')"

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

failed() {
  echo -n -e " [${RED}$1${NOCOLOR}]" | tee >(cat 1>&2)
  echo 1>&2
}

commit() {
  if [ $# -lt 1 ]; then
    echo "Cannot commit without message"
    exit 1
  fi
  message="$1"
  shift

  # skip if there are no changes
  if "$git" diff --quiet; then return 0; fi

  # run linting
  "$python_bin"/mypy --show-column-numbers github tests 1>&2
  "$python_bin"/pre-commit run --show-diff-on-failure --color=always --all-files 1>&2 || true

  # commit
  "$git" commit -a -m "$message" "$@" 1>&2
  echo 1>&2
  return 255
}

update() {
  # classes to update
  base="$1"; shift
  branch=
  if [ $# -gt 1 ]; then
    branch="$1"; shift
    if [ $# -eq 1 ]; then class="class"; else class="classes"; fi
  else
    branch="openapi/update-$1"
    class="class"
  fi
  classes="$*"

  # move to base branch
  "$git" checkout -f "$base" 1>&2

  # switch into class-specific branch
  if [[ $("$git" branch --list "$branch" | sed -E -e "s/^[*]? +//") != "" ]]; then
    "$git" branch -m "$branch" "$branch-$(date +%s)" 1>&2
  fi
  "$git" checkout -b "$branch" 1>&2

  # add schemas to class
  for github_class in $classes; do
    "$python" "$openapi" suggest --add "$spec" "$index" "$github_class" 1>&2
    echo 1>&2
  done || failed "adding schemas"
  commit "Add OpenAPI schemas to $class" && unchanged "schemas" || changed "schemas" "adding schemas"

  # update index
  "$python" "$openapi" index "$source_path" "$index" 1>&2

  # sort the class
  for github_class in $classes; do
    "$python" "$sort_class" "$github_class" 1>&2
    echo 1>&2
  done || failed "sorting $class"
  commit "Sort attributes and methods in $class" && unchanged "sorted" || changed "sorted" "sorting $class"

  # apply schemas to class
  for github_class in $classes; do
    "$python" "$openapi" apply "$spec" "$index" "$github_class" 1>&2
    echo 1>&2
  done || failed "applying schemas"
  commit "Updated $class according to API spec" && unchanged "$class" || changed "$class" "applying schemas"

  # apply schemas to test class
  for github_class in $classes; do
    if [ -f "tests/$github_class.py" ]; then
      "$python" "$openapi" apply --tests "$spec" "$index" "$github_class" 1>&2
      echo 1>&2
    fi
  done || failed "applying test schemas"
  commit "Updated test $class according to API spec" && unchanged "tests" || changed "tests" "applying test schemas"

  # fix test assertions
  for github_class in $classes; do
    filename="tests/$github_class.py"
    if [ -f "$filename" ]; then
      # reconstruct long lines
      "$python_bin"/pre-commit run --config "$pre_commit_conf" --file "$filename" || true
      "$update_assertions" "$filename" testAttributes 1>&2 || true
      # record test data for testAttributes, fix assertions, commit as separate commit
      # do not record for other tests (might delete things)
      echo 1>&2
    fi
  done
  commit "Updated test $class according to API spec" "--amend" && unchanged "assertions" || changed "assertions" "updating assertions"

  # run tests
  pass=none
  for github_class in $classes; do
    if [ -f "tests/$github_class.py" ]; then
      code=0
      "$python_bin"/pytest "tests/$github_class.py" -k testAttributes 1>&2 || code=$?
      if [ $code -eq 5 ]; then
        # ignore if testAttributes is missing
        continue
      elif [ $code -eq 0 ]; then
        # record class with successful test
        pass=true
      else
        # fail on first class with failing test
        pass=false
        break
      fi
    fi
  done
  if [ "$pass" == "true" ]; then unchanged "pass"; elif [ "$pass" == "false" ]; then failed "fail"; else echo -n -e " [${GREY}miss${NOCOLOR}]" | tee >(cat 1>&2); fi

  echo -e " ${BLUE}($branch)${NOCOLOR}" | tee >(cat 1>&2)
  "$git" checkout "$base" 1>&2
}


# memorize current base commit
base=$("$git" rev-parse --abbrev-ref HEAD)

# update index
echo -n "Updating index ($index)" | tee >(cat 1>&2)
"$python" "$openapi" index "$source_path" "$index" | while read -r line; do echo -n .; done
echo | tee >(cat 1>&2)

# update all classes
echo "Updating $(wc -w <<< "$github_classes") classes:" | tee >(cat 1>&2)
if [[ -n "$single_branch" ]]; then
  echo -n "$(wc -w <<< "$github_classes") PyGithub classes:" | tee >(cat 1>&2)
  update "$base" "$single_branch" $github_classes
else
  for github_class in $github_classes
  do
    echo -n "${spaces:${#github_class}}$github_class:" | tee >(cat 1>&2)
    update "$base" "$github_class"
  done
fi

# recreate index
echo -n "Updating index ($index)" | tee >(cat 1>&2)
"$python" "$openapi" index "$source_path" "$index" | while read -r line; do echo -n .; done
echo | tee >(cat 1>&2)
