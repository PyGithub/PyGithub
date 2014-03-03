#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import coverage


def main():
    cov = coverage.coverage(branch=True, omit=["/usr/*"])
    cov.start()
    import CodeGeneration
    import check
    CodeGeneration.main()
    check.main()
    cov.stop()
    cov.report()
    cov.html_report(directory="generation_coverage")


if __name__ == "__main__":
    main()
