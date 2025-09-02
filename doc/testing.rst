Testing
=======

Automated tests
---------------

First you need to install the test dependencies:

.. code-block:: bash

    pip install -r requirements/test.txt

Then you can run the tests through ``pytest tests``.

Run a specific test with

- ``pytest tests/tests_filename.py`` or
- ``pytest tests/tests_filename.py -k testMethod`` or
- ``pytest -k TestClass.testMethod``

To run manual tests with external scripts that use the PyGithub package, you can install your development version with:

.. code-block:: bash

    pip install --editable path/to/project

You may also want to use ``tox`` to run tests:

.. code-block:: bash

    pip install tox
    tox -epy313

Replay Data
-----------

Most of the tests call the Github REST API. For consistency, the test environment intercepts these calls,
asserts the calls are as expected, and return pre-recorded Github API data. The tests then assert those
data have the expected values.

Record replay data
~~~~~~~~~~~~~~~~~~

If you add or modify a test, for example ``Repository.testCompare``, you have record new replay data:

.. code-block:: bash

    pytest -k Repository.testCompare --record

This will create or update the ``tests/ReplayData/Repository.testCompare.txt`` file needed for your new test.
Add those files to git and commit them as well.

Reusing other tests' replay data
--------------------------------

Each test has its own replay data file. For instance, test ``Repository.testCompare`` uses
the replay data file ``tests/ReplayData/Repository.testCompare.txt``. If you want to avoid duplicate replay data files,
you can use the replay data file of another test:

.. code-block:: python

    class Repository(Framework.TestCase):
        def setUp(self):
            # this method uses file Repository.setUp.txt
            super().setUp()
            self.repo = self.g.get_repo("PyGithub/PyGithub")

        def testCompare(self):
            # this method uses file Repository.testCompare.txt
            comparison = self.repo.compare("v0.6", "v0.7")
            self.assertEqual(comparison.status, "ahead")

        def testCompare2(self):
            # this method would use file Repository.testCompare2.txt
            # but here we explicitly reuse a different file
            with self.replayData("Repository.testCompare.txt"):
                comparison = self.repo.compare("v0.6", "v0.7")
                self.assertEqual(comparison.status, "ahead")

Authenticating tests
~~~~~~~~~~~~~~~~~~~~

Most Github API calls require authentication. To record test replay data, a ``GithubCredentials.py`` file is needed
at the root of the project with the following contents:

.. code-block:: python

    oauth_token = "my_token"
    jwt = "my_json_web_token"               # Can be left empty if not used
    app_id = "my_app_id"                    # Can be left empty if not used
    app_private_key = "my_app_private_key"  # Can be left empty if not used

The ``oauth_token`` field in ``GithubCredentials.py`` is used by default to record test data.
Tests classes that require JWT (``jwt`` field), App authentication (``app_id`` and ``app_private_key`` field)
or no authentication at all, have to enable the respective auth mode in their ``setUp`` method.

Set ``self.authMode`` to ``"jwt"``, ``"app"`` and ``"none"``, respectively:

.. code-block:: python

    def setUp(self):
        self.authMode = "jwt"
        super().setUp()
        ...

An individual test method that needs a different authentication than configured in ``setUp`` can simply
create a new ``Github`` object with the respective authentication:

.. code-block:: python

    def setUp(self):
        self.authMode = "none"
        super().setUp()

    def testGetUserWithoutAuth(self):
        # this test uses no authentication
        self.assertEqual(self.g.get_user("jacquev6").name, "Vincent Jacques")

    def testGetUserWithOAuth(self):
        # this test needs OAuth authentication
        g = self.get_github("oauth_token")
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testGetUserWithJwt(self):
        # this test needs JWT authentication
        g = self.get_github("jwt")
        self.assertEqual(g.get_user("jacquev6").name, "Vincent Jacques")

    def testGetUserWithAppAuth(self):
        # this test needs App authentication
        g = self.get_github("app")
        self.assertEqual(g.get_user("jacquev6").name, "App name")

.. _update-assertions:

Updating assertions
-------------------

Once replay data have been created or updated, test assertions may fail because some values may have changed.
You can either manually update the expected values with the new values of your record data. Or you use the following commands
that attempt to perform this automatically:

.. code-block:: bash

    # prepare test for update-assertions.sh (turns multi-line assertions into single lines)
    python ./scripts/prepare-for-update-assertions.py

    # update expected values with actual values
    # please fix lines manually that the script cannot fix your you, then run this again
    ./scripts/update-assertions.sh tests/Repository.py testCompare

    # reformat test files (re-create multi-line assertions where needed)
    pre-commit run --all-files
