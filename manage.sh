#!/bin/bash
# -*- coding: utf-8 -*-

function publish {
    check
    test
    bump
    readme
    doc
    push
}

function check {
    pep8 --ignore=E501 github setup.py || exit
}

function check_copyright {
    for file in $(git ls-files | grep "py$")
    do
        git log "--format=format:# Copyright %ad %an %ae" --date=short -- $file |
        sed "s/\([0-9][0-9][0-9][0-9]\)-[0-9][0-9]-[0-9][0-9]/\1/g" | sort -u |
        while read copyright
        do
            if grep -n $file -e "^$copyright$" > /dev/null
            then
                echo > /dev/null
            else
                echo "$file should contain '$copyright'"
            fi
        done
    done
}

function test {
    # python3 setup.py test --quiet || exit

    coverage run --branch --include=github/*.py --omit=github/tests/*.py setup.py test --quiet || exit
    coverage report --show-missing || exit
}

function bump {
    previousVersion=$( grep '^version =' setup.py | sed 's/version = \"\(.*\)\"/\1/' )
    echo "Next version number? (previous: '$previousVersion')"
    read version
    sed -i -b "s/version = .*/version = \"$version\"/" setup.py
}

function readme {
    git log v$previousVersion.. --oneline

    echo "Edit README.rst and doc/changes.rst now, then press enter"
    read foobar
}

function doc {
    rm -rf doc/build
    mkdir doc/build
    cd doc/build
    git init
    sphinx-build -b html -d doctrees .. . || exit
    touch .nojekyll
    echo /doctrees/ > .gitignore
    git add . || exit
    git commit --message "Automatic generation" || exit
    git push --force ../.. HEAD:gh-pages || exit
    cd ../..
}

function push {
    echo "Break (Ctrl+c) here if something is wrong. Else, press enter"
    read foobar

    git commit -am "Publish version $version"

    cp COPYING* github
    python setup.py sdist upload
    rm -rf github/COPYING*

    git tag -m "Version $version" v$version

    git push github master master:develop
    git push --force github gh-pages
    git push --tags
}

function unmerged {
    BRANCHES_NOT_TO_BE_MERGED="-e gh-pages -e topic/DependencyGraph"
    COMMITS_NOT_TO_BE_MERGED="-e 1bea00a -e 11aeaa7 -e dd1e255 -e 670c6fb -e ed87a91 -e 072fbcb -e 421a743 -e 0c45af7 -e 92e4df4 -e 79ebd4b -e 0965ffd -e e1990c5 -e 55f3250"

    for b in `git branch -a --no-merged | grep -v $BRANCHES_NOT_TO_BE_MERGED`
    do
        if git --no-pager log ..$b --oneline | grep -v $COMMITS_NOT_TO_BE_MERGED > /dev/null
        then
            echo $b
            git --no-pager log ..$b --oneline
            echo
        fi
    done
}

$1
