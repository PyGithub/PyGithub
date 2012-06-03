#!/bin/sh

rm -f $(find . -name "*.pyc")

cd test

coverage erase
coverage run --branch IntegrationTest.py

echo "=============="
echo "|| Coverage ||"
echo "=============="

coverage report -m --include=../github/*

coverage html --include=../github/*
