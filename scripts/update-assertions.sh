#!/bin/bash

set -euo pipefail

python_bin="$(dirname "$(which python3)")"
pytest="$python_bin/pytest"

if [ $# -ne 2 ]; then
  echo "Please provide test file and function"
  exit 1
fi

test_file="$1"
test_func="$2"

# python unittest package abbreviates actual and expected values on assertion errors
# pytest will execute the following code, which configures unittest to not abbreviate
cat > conftest.py << EOF
def pytest_configure(config):
    import unittest
    unittest.util._MAX_LENGTH = 10240
EOF

update_assertion() {
  read -r assertion_line
  read line_number_line
  if [[ -z "$assertion_line" ]]; then return; fi
  if [[ "$assertion_line" == *"AssertionError: assert {'Authorizati"* ]]; then
    echo "Failed due to authorization error" >&2
    return
  fi

  test_file="tests/$(basename "$test_file")"
  line_number="${line_number_line/$test_file:/}"
  line_number="${line_number/%: */}"
  echo "$line_number"

  if [[ "$assertion_line" == *"AttributeError"* ]]; then
    assertion_line="${assertion_line/E       AttributeError: /}"
    if [[ "$assertion_line" == "'NoneType' object has no attribute "* ]]; then
      attribute="${assertion_line/\'NoneType\' object has no attribute /}"
      attribute="${attribute//\'/}"
      sed -i -e "${line_number}s/\S*[(]\([^,]*\).$attribute,.*/self.assertIsNone(\1)/" "$test_file"
    fi
  else
    assertion_line="${assertion_line/E       AssertionError: /}"
    actual="${assertion_line/% != */}"
    expected="${assertion_line/#* != /}"
    actual="${actual//datetime\./}"
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
  fi
}

last_line_number=
while true; do
  line_number=$($pytest --color=no "$test_file" -k "$test_func" | grep -e AttributeError -e AssertionError | update_assertion || true)
  if [[ "$line_number" == "" ]]; then exit; fi
  if [[ "$line_number" == "$last_line_number" ]]; then
    echo "Could not fix assertion in line $line_number"
    exit 1
  fi
  echo "fixed assertion in line number $line_number"
  last_line_number="$line_number"
  sleep 1
done
