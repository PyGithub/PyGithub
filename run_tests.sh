#!/bin/sh

rm -f $(find -name "*.pyc")

coverage erase

for f in $(find -name "*Test.py")
do
    coverage run --append $f --quiet
    echo
done

coverage report -m --include=./*
