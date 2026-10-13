#!/bin/bash

set -euo pipefail

base=$(cd "$(dirname "$0")/.."; pwd)
async_dir="$base/async"

if [[ "$async_dir" != "/"* ]]
then
  async_dir="$PWD/$async_dir"
fi
echo "Syncing PyGithub project with PyGithub-async in $async_dir"

(cd "$base"; tar -cf - $(git ls-files | grep -v -e "^\." -e "^async" -e "^github" -e "^openapi" -e "^pyproject.toml$" -e "^tox.ini$" -e "^requirements/" -e "^scripts/" -e "^tests/.*\.py") | tar -xvf - -C "$async_dir/")
