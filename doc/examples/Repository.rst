Repository
==========

Get repository topics
---------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_topics()
    [u'pygithub', u'python', u'github', u'github-api']

Get count of stars
------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.stargazers_count
    2086

Get list of open issues
--------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> open_issues = repo.get_issues(state='open')
    >>> for issue in open_issues:
    ...     print(issue)
    ...
    Issue(title="How to get public events?", number=913)
    Issue(title="Prevent .netrc from overwriting Auth header", number=910)
    Issue(title="Cache fetch responses", number=901)
    Issue(title="Is suspended_users for github enterprise implemented in NamedUser?", number=900)
    Issue(title="Adding migration api wrapper", number=899)

Get all the labels of the repository
------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> labels = repo.get_labels()
    >>> for label in labels:
    ...     print(label)
    ...
    Label(name="Hacktoberfest")
    Label(name="WIP")
    Label(name="bug")
    Label(name="documentation")

Get all of the contents of the root directory of the repository
---------------------------------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_contents("")
    >>> for content_file in contents:
    ...     print(content_file)
    ...
    ContentFile(path=".github")
    ContentFile(path=".gitignore")
    ContentFile(path=".travis.yml")
    ContentFile(path="CONTRIBUTING.md")
    ContentFile(path="COPYING")
    ContentFile(path="COPYING.LESSER")
    ContentFile(path="MAINTAINERS")
    ContentFile(path="MANIFEST.in")
    ContentFile(path="README.md")
    ContentFile(path="doc")
    ContentFile(path="github")
    ContentFile(path="manage.sh")
    ContentFile(path="requirements.txt")
    ContentFile(path="scripts")
    ContentFile(path="setup.py")

Get all of the contents of the repository recursively
-----------------------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_contents("")
    >>> while len(contents) > 1:
    ...     file_content = contents.pop(0)
    ...     if file_content.type == "dir":
    ...         contents.extend(repo.get_contents(file_content.path))
    ...     else:
    ...         print(file_content)
    ...
    ContentFile(path=".gitignore")
    ContentFile(path=".travis.yml")
    ContentFile(path="CONTRIBUTING.md")
    ...
    ContentFile(path="github/tests/ReplayData/Team.testRepoPermission.txt")
    ContentFile(path="github/tests/ReplayData/Team.testRepos.txt")
    ContentFile(path="github/tests/ReplayData/UserKey.setUp.txt")

Get a specific content file
---------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_contents("README.md")
    >>> print(contents)
    ...
    ContentFile(path="README.md")

Create a new file in the repository
-----------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_file("test.txt", "test", "test", branch="test")
    {'content': ContentFile(path="test.txt"), 'commit': Commit(sha="5b584cf6d32d960bb7bee8ce94f161d939aec377")}

Update a file in the repository
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_contents("test.txt", ref="test")
    >>> repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")
    {'commit': Commit(sha="b06e05400afd6baee13fff74e38553d135dca7dc"), 'content': ContentFile(path="test.txt")}

Delete a file in the repository
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_contents("test.txt", ref="test")
    >>> repo.delete_file(contents.path, "remove test", contents.sha, branch="test")
    {'commit': Commit(sha="0f40b0b4f31f62454f1758d7e6b384795e48fd96"), 'content': NotSet}

Get the top 10 referrers over the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_top_referrers()

Get the top 10 popular contents over the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_top_paths()

Get number of clones and breakdown for the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_clones_traffic()
    >>> contents = repo.get_clones_traffic(per="week")

Get number of views and breakdown for the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_views_traffic()
    >>> contents = repo.get_views_traffic(per="week")

=======
======
Mark the notifications of the repository as read
------------------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.mark_notifications_as_read()
