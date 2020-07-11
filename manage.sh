#!/bin/bash
# -*- coding: utf-8 -*-

set -e

function publish {
    bump
    readme
    push
}

function check {
    flake8
}

function fix_headers {
    python scripts/fix_headers.py
}

function bump {
    previousVersion=$( grep '^version =' setup.py | sed 's/version = \"\(.*\)\"/\1/' )
    echo "Next version number? (previous: '$previousVersion')"
    read version
    if [ -z "$version" ]; then
        echo "empty version string"
        exit 1
    fi
    sed -i -b "s/version = .*/version = \"$version\"/" setup.py
}

function readme {
    # creates a changelog based on the commits from the previous version until now
    changelog=$(tail -n +6 doc/changes.rst)
    gitlog=$(git log v$previousVersion.. --oneline --pretty=format:'* %s (%h)' | grep -v "Merge")
    today=$(date "+(%B %d, %Y)")
    echo -e "Change log\n==========\n\nStable versions\n~~~~~~~~~~~~~~~\n\nVersion $version $today\n-----------------------------------\n\n$gitlog\n$changelog" > doc/changes.rst
}

function push {
    echo "Break (Ctrl+c) here if something is wrong. Else, press enter"
    read foobar

    git commit -am "Publish version $version"

    git tag -m "Version $version" v$version

    git push --tags ${REMOTE:-origin} master
}

$1
