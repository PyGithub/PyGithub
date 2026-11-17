#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Provide path as argument and OpenAPI spec via sdtin"
  exit 1
fi

api_path=".paths.\"$1\""

cat | jq $api_path
