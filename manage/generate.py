#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import coverage
import unittest


def main():
    cov = coverage.coverage(branch=True, omit=["/usr/*"])
    cov.start()
    import CodeGeneration
    import check
    if unittest.main(exit=False, module="CodeGeneration.ApiDefinition.Checker", argv=["test"]).result.wasSuccessful():
        CodeGeneration.main()
        check.main()
    cov.stop()
    cov.report(include=["manage/CodeGeneration/*"])
    cov.html_report(directory="coverage/code_generation", include=["manage/CodeGeneration/*"])


if __name__ == "__main__":
    main()
