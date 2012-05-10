#!/bin/sh

rm -f $(find . -name "*.pyc")

cd test

coverage erase
coverage run IntegrationTest.py

echo "=============="
echo "|| Coverage ||"
echo "=============="

coverage report -m --include=../src/*
