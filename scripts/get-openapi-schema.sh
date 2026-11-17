#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Provide path as argument and OpenAPI spec via sdtin"
  exit 1
fi

api_path="$1"
api_path="${api_path/\//.\"}"
api_path="${api_path//\//\".\"}\""
cat | jq "${api_path}"
