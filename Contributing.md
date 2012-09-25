Issues
======

A good issue includes a [short, self contained, correct example](http://sscce.org/) of the problem, something like:

    assert github.Github().get_user("jacquev6").name == "Vincent Jacques"

It is even better if you provide the debug logs associated with your issue.
Enable them with `github.enable_console_debug_logging()` and copy them in the body of the issue.
Warning, you may want to remove some private information (authentication information is removed, but there may be private stuff in the messages)

If for any reason you are not able to provide, open your issue anyway and we will see what is needed to solve your problem.

Pull requests
=============

PyGithub follows [pep8 Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/) except for line length.
So if you do heavy modifications, please check your code with [pep8 Python style guide checker](http://pypi.python.org/pypi/pep8), by running `pep8 --ignore=E501 github`.
