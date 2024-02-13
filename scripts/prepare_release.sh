#!/bin/bash

set -eo pipefail

# update file headers
python scripts/fix_headers.py

# creates a changelog based on the commits from the previous version until now
previousVersion=$(git tag -l --merged main | tail -n1)
changelog=$(tail -n +6 doc/changes.rst)
gitlog=$(git log $previousVersion.. --oneline --pretty=format:'* %s (%h)')
today=$(date "+(%B %d, %Y)")
echo -e "Change log\n==========\n\nStable versions\n~~~~~~~~~~~~~~~\n\nVersion ?.?.? $today\n-----------------------------------\n\n$gitlog\n$changelog" > doc/changes.rst
