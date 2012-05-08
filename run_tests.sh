#!/bin/sh

rm -f $(find -name "*.pyc")

coverage erase
coverage run NewIntegrationTest.py

echo "=============="
echo "|| Coverage ||"
echo "=============="

coverage report -m --include=./*
