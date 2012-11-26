#!/bin/sh
# -*- coding: utf-8 -*-

rm -rf doc/build
git clone . doc/build
cd doc/build
git checkout --orphan gh-pages
git rm -rf .

sphinx-build -b html -d doctrees .. .
touch .nojekyll
echo "/doctrees/" > .gitignore

git add .
git commit --message "Automatic generation" || echo
git push -f origin gh-pages
