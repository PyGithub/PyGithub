#!/bin/sh

rm -f $(find -name "*.pyc")

coverage erase

for f in $(find -name "*UnitTest.py")
do
    coverage run --append $f --quiet
    echo
done

coverage report -m --include=./*
echo

for f in $(find -name "*IntegrationTest.py")
do
    # python $f
    echo
done