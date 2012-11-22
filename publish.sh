#!/bin/sh
# -*- coding: utf-8 -*-

pep8 --ignore=E501 github *.py  # pip install pep8

python -3 setup.py test --quiet
python3 setup.py test --quiet

coverage run --branch "--include=build/lib.linux-x86_64-2.7/github/*.py" "--omit=build/lib.linux-x86_64-2.7/github/tests/*.py" setup.py test --quiet
coverage report --show-missing

previousVersion=$( grep 'version=' setup.py | sed 's/.*version=\"\(.*\)\".*/\1/' )
echo "Next version number? (previous: '$previousVersion')"
read version
sed -i -b "s/version=.*/version=\"$version\",/" setup.py
git add setup.py

git log v$previousVersion.. --oneline

echo "Edit ReadMe.md and doc/ChangeLog.md now, then press enter"
read foobar
git add ReadMe.md doc/ChangeLog.md

echo "Break (Ctrl+c) here if something is wrong. Else, press enter"
read foobar

git commit -m "Publish version $version"
git tag -m "Version $version" v$version

cp -r *.md doc COPYING* github
python setup.py sdist upload
rm -rf github/*.md github/doc github/COPYING*

git push github master master:develop
git push --tags
