#!/bin/sh

rm -f $(find -name "*.pyc")

coverage erase

for f in $(find -name "*IntegrationTest.py")
do
    coverage run --append $f
    echo
done

echo "====================================================="
echo "|| Coverage of integration tests (for information) ||"
echo "====================================================="
coverage report -m --include=./*
echo

coverage erase

for f in $(find -name "*UnitTest.py")
do
    coverage run --append $f --quiet
    echo
done

echo "============================================"
echo "|| Coverage of unit tests (shall be 100%) ||"
echo "============================================"
coverage report -m --include=./*
echo
