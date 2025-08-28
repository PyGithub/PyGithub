Github OpenAPI spec
===================

Adding classes, attributes or methods
-------------------------------------

Github provides an `OpenAPI specification for its v3 REST API <https://github.com/github/rest-api-description/>`__.
This can be used to semi-automate the creation and maintenance of PyGithub classes.

OpenAPI annotations
-------------------

PyGithub classes have annotations that link the code to the OpenAPI spec. This allows to automate keeping
the implementation in-sync with the specification.

PyGithub class annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~

PyGithub classes have annotations that link those classes to the respective schemas of the OpenAPI spec.

For example, the ``Repository`` class has this header:

.. code-block:: python

    class Repository(CompletableGithubObject):
        """
        This class represents Repositories.

        The reference can be found here
        https://docs.github.com/en/rest/reference/repos

        The OpenAPI schema can be found at

        - /components/schemas/event/properties/repo
        - /components/schemas/full-repository
        - /components/schemas/minimal-repository
        - /components/schemas/nullable-repository
        - /components/schemas/pull-request-minimal/properties/base/properties/repo
        - /components/schemas/pull-request-minimal/properties/head/properties/repo
        - /components/schemas/repository
        - /components/schemas/simple-repository

        """

The list of OpenAPI schemas can be found below the ``The OpenAPI schema can be found at`` line.

.. _get-openapi-schema:

A schema can easily be extracted from the OpenAPI spec as follows (this requires ``jq`` to be installed)::

    ./scripts/get-openapi-schema.sh "/components/schemas/minimal-repository" < api.github.com.2022-11-28.json

This outputs::

    {
      "title": "Minimal Repository",
      "description": "Minimal Repository",
      "type": "object",
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64",
          "example": 1296269
        },
        "node_id": {
          "type": "string",
          "example": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5"
        },
        "name": {
          "type": "string",
          "example": "Hello-World"
        },
        "full_name": {
          "type": "string",
          "example": "octocat/Hello-World"
        },
        …
    }

PyGithub method annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Methods of PyGithub classes are annotated with the API path that they call.

For example, the ``get_branch`` method of the ``Repository`` class has this header:

.. code-block:: python

    def get_branch(self, branch: str) -> Branch:
        """
        :calls: `GET /repos/{owner}/{repo}/branches/{branch} <https://docs.github.com/en/rest/reference/repos#get-a-branch>`_
        :param branch: string
        :rtype: :class:`github.Branch.Branch`
        """

This documents that the method calls the ``/repos/{owner}/{repo}/branches/{branch}`` API path using the ``GET`` verb.

.. _get-openapi-path:

A path can easily be extracted from the OpenAPI spec as follows (this requires ``jq`` to be installed)::

    ./scripts/get-openapi-path.sh "/repos/{owner}/{repo}/branches/{branch}" < api.github.com.2022-11-28.json

This outputs::

    {
      "get": {
        "summary": "Get a branch",
        "description": "",
        "tags": ["repos"],
        "operationId": "repos/get-branch",
        "externalDocs": {
          "description": "API method documentation",
          "url": "https://docs.github.com/rest/branches/branches#get-a-branch"
        },
        "parameters": […],
        "responses": {
          "200": {
            "description": "Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/branch-with-protection"
                },
                "examples": {
                  "default": {
                    "$ref": "#/components/examples/branch-get"
                  }
                }
              }
            }
          },
          "301": {
            "$ref": "#/components/responses/moved_permanently"
          },
          "404": {
            "$ref": "#/components/responses/not_found"
          }
        },
        …
      }
    }

The OpenAPI sync CLI
--------------------

The main script to leverage the OpenAPI spec is the ``scripts/openapi.py`` CLI.

Run ``python scripts/openapi.py --help`` or ``python scripts/openapi.py COMMAND --help`` for help::

    usage: openapi.py [-h] [--dry-run] [--exit-code] [--verbose] {fetch,index,suggest,apply,create} ...

    Applies OpenAPI spec to PyGithub GithubObject classes

    positional arguments:
      {fetch,index,suggest,apply,create}

    options:
      -h, --help            show this help message and exit
      --dry-run             Show prospect changes and do not modify any files (default: False)
      --exit-code           Indicate changes via non-zeor exit code (default: False)
      --verbose             Provide more information (default: False)

Setup OpenAPI support
---------------------

Download the OpenAPI specification, e.g. version ``2022-11-28`` for the ``api.github.com`` API::

    python scripts/openapi.py fetch api.github.com 2022-11-28 api.github.com.2022-11-28.json

Load the PyGithub sources into an index file, e.g. ``openapi.index``::

    python scripts/openapi.py index github api.github.com.2022-11-28.json openapi.index

Automatically add schemas to PyGithub classes
---------------------------------------------

TODO: intro::

    python scripts/openapi.py suggest schemas --add api.github.com.2022-11-28.json openapi.index Commit

This may produce the following changes::

    diff --git a/github/Commit.py b/github/Commit.py
    index 7a2ac9d0..2ae31d07 100644
    --- a/github/Commit.py
    +++ b/github/Commit.py
    @@ -89,6 +89,7 @@ class Commit(CompletableGithubObject):
         The OpenAPI schema can be found at

         - /components/schemas/branch-short/properties/commit
    +    - /components/schemas/commit
         - /components/schemas/commit-search-result-item/properties/parents/items
         - /components/schemas/commit/properties/parents/items
         - /components/schemas/short-branch/properties/commit


Once new schemas have been added to classes, these schemas should be applied next. Only applying the
schemas will add new attributes to the class.

.. _apply-schemas:

Automatically apply schemas to PyGithub classes
-----------------------------------------------

After new schemas have been added to PyGithub classes, or a new OpenAPI spec has been downloaded,
the schemas can be applied to PyGithub classes as follows.

First update the index, then apply the schemas (here to class ``Commit`` only)::

    python scripts/openapi.py index github api.github.com.2022-11-28.json openapi.index
    python scripts/openapi.py apply --tests --new-schemas create-class github api.github.com.2022-11-28.json openapi.index Commit

This may produce the following changes::

    diff --git a/github/Commit.py b/github/Commit.py
    index 84cb78eb..2ae31d07 100644
    --- a/github/Commit.py
    +++ b/github/Commit.py
    @@ -100,6 +100,7 @@ class Commit(CompletableGithubObject):
         def _initAttributes(self) -> None:
             self._author: Attribute[NamedUser] = NotSet
             self._comments_url: Attribute[str] = NotSet
    +        self._commit: Attribute[GitCommit] = NotSet
             self._committer: Attribute[NamedUser] = NotSet
             self._files: Attribute[list[File]] = NotSet
             self._html_url: Attribute[str] = NotSet
    @@ -128,6 +129,11 @@ class Commit(CompletableGithubObject):
             self._completeIfNotSet(self._comments_url)
             return self._comments_url.value

    +    @property
    +    def commit(self) -> GitCommit:
    +        self._completeIfNotSet(self._commit)
    +        return self._commit.value
    +
         @property
         def committer(self) -> NamedUser:
             self._completeIfNotSet(self._committer)
    @@ -332,6 +338,8 @@ class Commit(CompletableGithubObject):
                 self._author = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["author"])
             if "comments_url" in attributes:  # pragma no branch
                 self._comments_url = self._makeStringAttribute(attributes["comments_url"])
    +        if "commit" in attributes:  # pragma no branch
    +            self._commit = self._makeClassAttribute(github.GitCommit.GitCommit, attributes["commit"])
             if "committer" in attributes:  # pragma no branch
                 self._committer = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["committer"])
             if "files" in attributes:  # pragma no branch

With option ``--tests``, tests will also be modified.

Some attributes may return schemas that are not implemented by any PyGithub class. In that case,
option ``--new-schemas create-class`` will creates all those classes.

Create a PyGithub class from an OpenAPI schema
----------------------------------------------

New PyGithub classes returned by other PyGithub classes' attributes can be created by applying the schemas of the latter class
via ``scripts/openapi.py apply --new-schemas create-class …``. See :ref:`apply-schemas` for details.

New PyGithub classes returned by other PyGithub classes' methods can be created based on the Github REST API path
of the method.

Given a Github REST API path like ``/app``, you can extract the ``GET`` response from the OpenAPI spec via::

    ./scripts/get-openapi-path.sh "/app" < api.github.com.2022-11-28.json

The JSON path ``'.get.responses."200".content'`` provides details about the response schema::

    ./scripts/get-openapi-path.sh "/app" < api.github.com.2022-11-28.json | jq '.get.responses."200".content'
    {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/integration"
        },
        …
      }
    }

A new PyGithub can be created from an OpenAPI schema as follows.

First, update the index, then create the class::

    python scripts/openapi.py index github api.github.com.2022-11-28.json openapi.index
    python scripts/openapi.py create class --tests --new-schemas create-class \
      github api.github.com.2022-11-28.json openapi.index \
      AuthenticatedApp https://docs.github.com/en/rest/reference/apps#get-the-authenticated-app \
      /components/schemas/integration

The Github docs URL (in above example ``https://docs.github.com/en/rest/reference/apps#get-the-authenticated-app``)
can be obtained from the OpenAPI spec via JSON path ``'.get.externalDocs.url'``::

    ./scripts/get-openapi-path.sh "/app" < api.github.com.2022-11-28.json | jq '.get.externalDocs.url'
    "https://docs.github.com/rest/apps/apps#get-the-authenticated-app"

This would create the following PyGithub class (``github/AuthenticatedApp.py``)::

    ############################ Copyrights and license ############################
    …
    ################################################################################

    from __future__ import annotations

    from typing import Any, TYPE_CHECKING
    from datetime import datetime, timezone

    import github.NamedUser
    from github.GithubObject import NonCompletableGithubObject
    from github.GithubObject import Attribute, NotSet

    if TYPE_CHECKING:
        from github.GithubObject import NonCompletableGithubObject
        from github.NamedUser import NamedUser


    class AuthenticatedApp(NonCompletableGithubObject):
        """
        This class represents AuthenticatedApp.

        The reference can be found here
        https://docs.github.com/en/rest/reference/apps#get-the-authenticated-app

        The OpenAPI schema can be found at
        - /components/schemas/integration

        """

        def _initAttributes(self) -> None:
            self._client_id: Attribute[str] = NotSet
            self._created_at: Attribute[datetime] = NotSet
            …
            self._owner: Attribute[NamedUser] = NotSet
            self._slug: Attribute[str] = NotSet
            self._updated_at: Attribute[datetime] = NotSet

        def __repr__(self) -> str:
            # TODO: replace "some_attribute" with uniquely identifying attributes in the dict, then run:
            return self.get__repr__({"some_attribute": self._some_attribute.value})

        @property
        def client_id(self) -> str:
            return self._client_id.value

        @property
        def created_at(self) -> datetime:
            return self._created_at.value

        @property
        def owner(self) -> NamedUser:
            return self._owner.value

        @property
        def slug(self) -> str:
            return self._slug.value

        @property
        def updated_at(self) -> datetime:
            return self._updated_at.value

        def _useAttributes(self, attributes: dict[str, Any]) -> None:
            # TODO: remove if parent does not implement this
            super()._useAttributes(attributes)
            if "client_id" in attributes:  # pragma no branch
                self._client_id = self._makeStringAttribute(attributes["client_id"])
            if "created_at" in attributes:  # pragma no branch
                self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
            …
            if "owner" in attributes:  # pragma no branch
                self._owner = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["owner"])
            if "slug" in attributes:  # pragma no branch
                self._slug = self._makeStringAttribute(attributes["slug"])
            if "updated_at" in attributes:  # pragma no branch
                self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])

As well as the following PyGithub test class (``tests/AuthenticatedApp.py``)::

    ############################ Copyrights and license ############################
    …
    ################################################################################

    from __future__ import annotations

    from datetime import datetime, timezone

    from . import Framework


    class AuthenticatedApp(Framework.TestCase):
        def setUp(self):
            super().setUp()
            # TODO: create an instance of type AuthenticatedApp and assign to self.attr, then run:
            #   pytest ./tests/AuthenticatedApp.py -k testAttributes --record
            #   ./scripts/update-assertions.sh ./tests/AuthenticatedApp.py testAttributes
            #   pre-commit run --all-files
            self.attr = None

        def testAttributes(self):
            self.assertEqual(self.attr.client_id, "")
            self.assertEqual(self.attr.created_at, datetime(2020, 1, 2, 12, 34, 56, tzinfo=timezone.utc))
            …
            self.assertEqual(self.attr.slug, "")
            self.assertEqual(self.attr.updated_at, datetime(2020, 1, 2, 12, 34, 56, tzinfo=timezone.utc))
            self.assertEqual(self.attr.url, "")


Complete setUp::

    def setUp(self):
        self.authMode = "app"  # usually not needed
        super().setUp()
        self.app = self.g.get_app()  # the method that returns the tested class

and replace ``self.attr`` with ``self.app`` in ``testAttributes``.

record test data::

    pytest ./tests/AuthenticatedApp.py -k testAttributes --record

once you see the first ``AssertionError``, update assertions in testAttributes::

    ./scripts/update-assertions.sh tests/AuthenticatedApp.py testAttributes

test::

    pytest tests/AuthenticatedApp.py

Create a PyGithub method from an OpenAPI path
---------------------------------------------

Methods can be added to PyGithub classes via the ``scripts/openapi.py`` script.

First update the index, then create a method::

    python scripts/openapi.py index github api.github.com.2022-11-28.json openapi.index
    python scripts/openapi.py create method \
      api.github.com.2022-11-28.json openapi.index \
      AuthenticatedApp get_installations GET /app/installations

Adds the method ``get_installations`` to ``github/AuthenticatedApp.py``::

    def get_installations(self) -> list[Installation]:
        """
        :calls: `GET /app/installations <https://docs.github.com/rest/apps/apps#list-installations-for-the-authenticated-app>`_
        :rtype: list[github.Installation.Installation]

        List installations for the authenticated app.
        """
        headers, data = self._requester.requestJsonAndCheck("GET", f"{self.url}/installations")
        return data
