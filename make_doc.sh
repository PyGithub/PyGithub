#!/bin/sh
# -*- coding: utf-8 -*-

rm -rf doc/build
mkdir doc/build
cd doc/build
git init

sphinx-build -b html -d doctrees .. .
touch .nojekyll
echo "/doctrees/" > .gitignore

git add .
git commit --message "Automatic generation" || echo
git push -f ../.. HEAD:gh-pages
