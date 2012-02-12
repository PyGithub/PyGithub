#!/bin/sh

rm -f $(find -name "*.pyc")

coverage erase

for f in *Test.py
do
    coverage run --append $f --quiet
    echo
done

coverage report -m --include=./*
