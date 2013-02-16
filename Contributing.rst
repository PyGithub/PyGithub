Contributing
============

Issues
------

A good issue includes a `short, self contained, correct example <http://sscce.org/>`_ of the problem, something like::

    assert github.Github().get_user("jacquev6").name == "Vincent Jacques"

It is even better if you provide the debug logs associated with your issue.
Enable them with :func:`github.enable_console_debug_logging` and copy them in the body of the issue.
Warning, you may want to remove some private information (authentication information is removed, but there may be private stuff in the messages)

If for any reason you are not able to do that, open your issue anyway and we will see what is needed to solve your problem.

Pull requests
-------------

Please do your pull requests on the ``develop`` branch.

Automated tests
~~~~~~~~~~~~~~~

You can run the tests through ``python -m github.tests``. Run a specific test with ``python -m github.tests TestCase`` or ``python -m github.tests TestCase.testMethod``.

If you add a new test, for example ``Issue139.testCompletion``, you must add an import in ``github/tests/AllTests.py``. Then, you have to run ``python -m github.tests Issue139.testCompletion --record`` to create the ``github/tests/ReplayData/*.txt`` files needed for you new test. Check them and commit them as well. You will need a ``GithubCredentials.py`` file at the root of the project with the following contents::

	login = "my_login"
	password = "my_password"
	oauth_token = "my_token"  # Can be left empty if not used

Coding conventions
~~~~~~~~~~~~~~~~~~

PyGithub follows `pep8 Style Guide for Python Code <http://www.python.org/dev/peps/pep-0008/>`_ except for line length.
Please check your code with `pep8 Python style guide checker <http://pypi.python.org/pypi/pep8>`_, by running ``pep8 --ignore=E501 github``.
