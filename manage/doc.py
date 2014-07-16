#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import subprocess
import os
import shutil
import glob


def main():
    if os.path.exists("gh-pages"):
        shutil.rmtree("gh-pages")
    if os.path.exists("doc/doctrees"):
        shutil.rmtree("doc/doctrees")

    subprocess.check_call([
        "git",
        "branch",
        "-f",
        "gh-pages",
        "github/gh-pages",
    ])

    subprocess.check_call([
        "git",
        "clone",
        ".",
        "gh-pages",
        "-b", "gh-pages",
    ])

    os.chdir("gh-pages")

    for f in glob.glob(os.path.join("..", "doc", "*.dot")):
        subprocess.check_call([
            "dot",
            "-Tpng",
            f,
            "-O"
        ])

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
