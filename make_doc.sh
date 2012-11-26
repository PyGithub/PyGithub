#!/bin/sh
# -*- coding: utf-8 -*-

rm -rf doc/build
git clone . doc/build/html
cd doc/build/html
git checkout generated-doc
git rm -rf .

sphinx-build -b html -d ../../build/doctrees ../.. .

git add .
git commit --message "Automatic generation" || echo
git checkout gh-pages
( git merge generated-doc --message "Update Github pages with generated doc" && git push origin generated-doc gh-pages ) || echo "Something went wrong. cd doc/build/html; git mergetool; git commit; git push"
