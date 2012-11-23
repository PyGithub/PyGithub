#!/bin/sh
# -*- coding: utf-8 -*-

rm -rf doc/build
git clone --branch generated-doc git@github.com:jacquev6/PyGithub.git doc/build/html

cd doc/build/html
git rm -rf .

cd ../..
sphinx-build -b html -d build/doctrees source build/html
cd build/html

git add .
git commit --allow-empty --message "Automatic generation"
git push
git checkout gh-pages
( git merge --no-ff generated-doc --message "Update Github pages with generated doc" && git push ) || echo "Something went wrong. cd doc/build/html; git mergetool; git commit; git push"
