#!/bin/sh
# -*- coding: utf-8 -*-

python setup.py publish || exit

previousVersion=$( grep '^version =' setup.py | sed 's/version = \"\(.*\)\"/\1/' )
echo "Next version number? (previous: '$previousVersion')"
read version
sed -i -b "s/version = .*/version = \"$version\"/" setup.py
git add setup.py

git log v$previousVersion.. --oneline

echo "Edit ReadMe.rst and doc/changes.rst now, then press enter"
read foobar
git add ReadMe.rst doc/changes.rst

git commit -m "Publish version $version"

cp -r doc COPYING* github
python setup.py sdist upload
rm -rf github/*.md github/doc github/COPYING*

echo "Break (Ctrl+c) here if something is wrong. Else, press enter"
read foobar

git tag -m "Version $version" v$version

git push github master master:develop gh-pages
git push --tags
