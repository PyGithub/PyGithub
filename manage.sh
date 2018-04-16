#!/bin/bash
# -*- coding: utf-8 -*-

function publish {
    bump
    readme
    push
}

function check {
    pep8 --ignore=E501 github scripts doc *.py || exit
}

function fix_headers {
    python scripts/fix_headers.py
}

function test {
    test2
    test3
}

function test2 {
    coverage run --branch --include=github/*.py --omit=github/tests/*.py setup.py test --quiet || exit
    coverage report --show-missing || exit
}

function test3 {
    python3 setup.py test --quiet || exit
}

function bump {
    previousVersion=$( grep '^version =' setup.py | sed 's/version = \"\(.*\)\"/\1/' )
    echo "Next version number? (previous: '$previousVersion')"
    read version
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

    git push origin master
    git push --tags
}

$1
