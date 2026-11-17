Scripts
=======

All scripts are located in the ``scripts/`` directory.

Script ``openapi.py``
---------------------

The main script to sync PyGithub classes with the Github OpenAPI spec.

Run ``scripts/openapi.py --help`` or ``scripts/openapi.py COMMAND --help`` for help::

    usage: openapi.py [-h] [--dry-run] [--exit-code] [--verbose] {fetch,index,suggest,apply,create} ...

    Applies OpenAPI spec to PyGithub GithubObject classes

    positional arguments:
      {fetch,index,suggest,apply,create}

    options:
      -h, --help            show this help message and exit
      --dry-run             Show prospect changes and do not modify any files (default: False)
      --exit-code           Indicate changes via non-zeor exit code (default: False)
      --verbose             Provide more information (default: False)

See :doc:`openapi` for details.

Script ``sort_class.py``
------------------------

The ``scripts/openapi.py`` script works best when attributes and methods are sorted.

This script applies that order to all / to specific classes::

    usage: sort_class.py [-h] [--dry-run] index_filename class_name [class_name ...]

    Sorts methods of GithubObject classes, also sorts attributes in _initAttributes and _useAttributes

    positional arguments:
      index_filename  Path of index file
      class_name      GithubObject class to sort, e.g. HookDelivery or github.HookDelivery.HookDeliverySummary

    options:
      -h, --help      show this help message and exit
      --dry-run       show prospect changes and do not modify the file


See :doc:`openapi` for details.

Script ``get-openapi-path.sh``
------------------------------

Quickly extract a specific Github API path from the OpenAPI spec. See :ref:`Get an OpenAPI API path <get-openapi-path>`.

This script requires `jq <https://jqlang.github.io/jq/>`__ to be installed.

Script ``get-openapi-schema.sh``
--------------------------------

Quickly extract a specific OpenAPI schema from the spec. See :ref:`Get an OpenAPI schema <get-openapi-schema>`.

This script requires `jq <https://jqlang.github.io/jq/>`__ to be installed.

Script ``openapi-update-classes.sh``
------------------------------------

An umbrella script that syncs all / specific classes with the OpenAPI spec.

Invoke the script::

    ./scripts/openapi-update-classes.sh [--create-classes] [--branch BRANCH] [--branch-prefix BRANCH_PREFIX] [CLASS_NAME ...]

The script puts all changes into either a single branch (``--branch BRANCH``),
or one branch per PyGithub class (``--branch-prefix BRANCH_PREFIX`` prefixes branches
with ``BRANCH_PREFIX``, default is ``openapi/update``).

With ``--create-classes``, the script creates new PyGithub classes for any schema returned by an attribute
that is not yet implemented by a PyGithub class.

Script ``prepare-for-update-assertions.py``
-------------------------------------------

Prepares a test method to be called with ``scripts/update-assertions.sh``.

Run ``scripts/update-assertions.sh --help`` for help::

    usage: prepare-for-update-assertions.py [-h] [--dry-run] [--exit-code] filename function

    Removes newlines from all statements in a specific function of one test file

    positional arguments:
      filename     Path of test file
      function     Name of the test function

    options:
      -h, --help   show this help message and exit
      --dry-run    Show prospect changes and do not modify the file
      --exit-code  Indicate changes via non-zero exit code

See :ref:`update-assertions` for details.

Script ``update-assertions.sh``
-------------------------------

Updates all assertions' expected values with actual values. This is useful to mass-update assertions when
actual data changed for tests.

Invoke the script::

    ./scripts/update-assertions.sh TEST_FILE TEST_METHOD

See :ref:`update-assertions` for details.

Script ``prepare_release.sh``
-----------------------------

Script to prepare a release.

Script ``fix_headers.py``
-------------------------

Updates the licence header of all files. This is used as part of the release process.
