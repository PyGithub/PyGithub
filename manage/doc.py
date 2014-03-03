#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import subprocess
import os
import shutil


def main():
    if os.path.exists("gh-pages"):
        os.chdir("gh-pages")
        subprocess.check_call([
            "git",
            "pull",
            "--ff-only",
        ])
    else:
        subprocess.check_call([
            "git",
            "clone",
            ".",
            "gh-pages",
            "-b", "gh-pages",
        ])
        os.chdir("gh-pages")

    subprocess.check_call([
        "sphinx-build",
        "-b",
        "html",
        "-d",
        "../doc/doctrees",
        "../doc",
        "v2",
    ])

    subprocess.check_call([
        "git",
        "add",
        ".",
        "--all",
    ])

    subprocess.check_call([
        "git",
        "commit",
        "-m", "Generate doc of v2",
    ])

    subprocess.check_call([
        "git",
        "push",
        "origin",
        "gh-pages"
    ])


if __name__ == "__main__":
    main()
