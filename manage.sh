#!/bin/bash
# -*- coding: utf-8 -*-

function publish {
    check
    test
    bump
    readme
    doc
    push
    # twitt_release
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
    git log v$previousVersion.. --oneline

    echo "Edit README.rst and doc/changes.rst now, then press enter"
    read foobar
}

function doc {
    rm -rf gh-pages
    git clone . gh-pages -b gh-pages || exit
    sphinx-build -b html -d doc/doctrees doc gh-pages/v1 || exit

    cd gh-pages
    git add . --all || exit
    git commit --message "Generate doc of v1" || exit
    git push origin gh-pages || exit
    cd ..
}

function push {
    echo "Break (Ctrl+c) here if something is wrong. Else, press enter"
    read foobar

    git commit -am "Publish version $version"

    sdist_upload

    git tag -m "Version $version" v$version

    git push github master master:develop gh-pages
    git push --tags
}

function sdist_upload {
    python setup.py sdist upload
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

function compare_to_api_ref_doc {
    if [ -e developer.github.com ]
    then
        cd developer.github.com
        git pull
        cd ..
    else
        git clone https://github.com/github/developer.github.com.git
    fi
    python scripts/compare_to_api_ref_doc.py
}

function twitt_release {
    python scripts/twitt_release.py $version
}

$1
