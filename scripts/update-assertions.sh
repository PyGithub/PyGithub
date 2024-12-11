#!/bin/bash

set -euo pipefail

python_bin="../venv-PyGithub/bin"
pytest="$python_bin/pytest"

if [ $# -ne 2 ]; then
  echo "Please provide test file and function"
  exit 1
fi

test_file="$1"
test_func="$2"

update_assertion() {
  read assertion_line
  read line_number_line
  if [[ -z "$assertion_line" ]]; then return; fi
  #echo $assertion_line
  #echo $line_number_line
  assertion_line="${assertion_line/E       AssertionError: /}"
  actual="${assertion_line/% != */}"
  expected="${assertion_line/#* != /}"
  line_number="${line_number_line/$test_file:/}"
  line_number="${line_number/%: */}"
  actual="${actual//datetime\./}"
  #echo "$actual" >&2
  #echo "$expected" >&2
  #echo "$line_number" >&2
  echo "$line_number"
  if [ "$actual" == "None" ]; then
    sed -i -e "${line_number}s/\S*[(]\([^,]*\),.*/self.assertIsNone(\1)/" "$test_file"
  elif [[ "$actual" == "'"*"["*" chars]"*"'" ]]; then
    prefix="${actual%%[*}"
    repl=$(sed -e "s/\([$.*[\/^]\)/\\\\\1/g" <<< "$prefix${prefix:0:1}")
    sed -i -e "${line_number}s/\S*[(]\([^,]*\), .*[)]/self.assertTrue(\1.startswith($repl))/" "$test_file"
  else
    repl=$(sed -e "s/\([$.*[\/^]\)/\\\\\1/g" <<< "$actual")
    sed -i -e "${line_number}s/[(]\([^,]*\), .*[)]/(\1, $repl)/" "$test_file"
  fi
}

last_line_number=
while true; do
  line_number=$($pytest --color=no "$test_file" -k "$test_func" | grep AssertionError | update_assertion || true)
  if [[ "$line_number" == "" ]]; then exit; fi
  if [[ "$line_number" == "$last_line_number" ]]; then
    echo "Could not fix assertion in line $line_number"
    exit 1
  fi
  echo "fixed assertion in line number $line_number"
  last_line_number="$line_number"
  sleep 1
done
