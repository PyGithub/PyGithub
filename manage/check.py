#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import subprocess


def main():
    subprocess.check_call([
        "pep8",
        "--ignore=E501",
        ".",
    ])


if __name__ == "__main__":
    main()
