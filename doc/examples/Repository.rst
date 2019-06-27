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
    >>> repo.create_file("/test.txt", "test", "test", branch="test")
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
    >>> print(contents)
    [
      Referrer(referrer="Google", count=4, uniques=3),
      Referrer(referrer="stackoverflow.com", count=2, uniques=2),
      Referrer(referrer="eggsonbread.com", count=1, uniques=1),
      Referrer(referrer="yandex.ru", count=1, uniques=1)
    ]

Get the top 10 popular contents over the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_top_paths()
    >>> print(contents)
    [
      Path(path="/github/hubot", title="github/hubot: A customizable life embetterment robot.", count=3542, uniques=2225),
      Path(path="/github/hubot/blob/master/docs/scripting.md", title="hubot/scripting.md at master · github/hubot · GitHub", count=1707, uniques=804),
      Path(path="/github/hubot/tree/master/docs", title="hubot/docs at master · github/hubot · GitHub", count=685, uniques=435),
      Path(path="/github/hubot/tree/master/src", title="hubot/src at master · github/hubot · GitHub", count=577, uniques=347),
      Path(path="/github/hubot/blob/master/docs/index.md", title="hubot/index.md at master · github/hubot · GitHub", count=379, uniques=259),
      Path(path="/github/hubot/blob/master/docs/adapters.md", title="hubot/adapters.md at master · github/hubot · GitHub", count=354, uniques=201),
      Path(path="/github/hubot/tree/master/examples", title="hubot/examples at master · github/hubot · GitHub", count=340, uniques=260),
      Path(path="/github/hubot/blob/master/docs/deploying/heroku.md", title="hubot/heroku.md at master · github/hubot · GitHub", count=324, uniques=217),
      Path(path="/github/hubot/blob/master/src/robot.coffee", title="hubot/robot.coffee at master · github/hubot · GitHub", count=293, uniques=191),
      Path(path="/github/hubot/blob/master/LICENSE.md", title="hubot/LICENSE.md at master · github/hubot · GitHub", count=281, uniques=222)
    ]

Get number of clones and breakdown for the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_clones_traffic()
    >>> contents = repo.get_clones_traffic(per="week")
    >>> print(contents)
    {
      "count": 173,
      "uniques": 128,
      "clones": [
        Clones(timestamp=2016-10-10 00:00:00, count=2, uniques=1),
        Clones(timestamp=2016-10-11 00:00:00, count=17, uniques=16),
        Clones(timestamp=2016-10-12 00:00:00, count=21, uniques=15),
        Clones(timestamp=2016-10-13 00:00:00, count=8, uniques=7),
        Clones(timestamp=2016-10-14 00:00:00, count=5, uniques=5),
        Clones(timestamp=2016-10-15 00:00:00, count=2, uniques=2),
        Clones(timestamp=2016-10-16 00:00:00, count=8, uniques=7),
        Clones(timestamp=2016-10-17 00:00:00, count=26, uniques=15),
        Clones(timestamp=2016-10-18 00:00:00, count=19, uniques=17),
        Clones(timestamp=2016-10-19 00:00:00, count=19, uniques=14),
        Clones(timestamp=2016-10-20 00:00:00, count=19, uniques=15),
        Clones(timestamp=2016-10-21 00:00:00, count=9, uniques=7),
        Clones(timestamp=2016-10-22 00:00:00, count=5, uniques=5),
        Clones(timestamp=2016-10-23 00:00:00, count=6, uniques=5),
        Clones(timestamp=2016-10-24 00:00:00, count=7, uniques=5)
      ]
    }

Get number of views and breakdown for the last 14 days
-------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> contents = repo.get_views_traffic()
    >>> contents = repo.get_views_traffic(per="week")
    >>> print(contents)
    {
      "count": 14850,
      "uniques": 3782,
      "views": [
        View(timestamp=2016-10-10 00:00:00, count=440, uniques=143),
        View(timestamp=2016-10-11 00:00:00, count=1308, uniques=414),
        View(timestamp=2016-10-12 00:00:00, count=1486, uniques=452),
        View(timestamp=2016-10-13 00:00:00, count=1170, uniques=401),
        View(timestamp=2016-10-14 00:00:00, count=868, uniques=266),
        View(timestamp=2016-10-15 00:00:00, count=495, uniques=157),
        View(timestamp=2016-10-16 00:00:00, count=524, uniques=175),
        View(timestamp=2016-10-17 00:00:00, count=1263, uniques=412),
        View(timestamp=2016-10-18 00:00:00, count=1402, uniques=417),
        View(timestamp=2016-10-19 00:00:00, count=1394, uniques=424),
        View(timestamp=2016-10-20 00:00:00, count=1492, uniques=448),
        View(timestamp=2016-10-21 00:00:00, count=1153, uniques=332),
        View(timestamp=2016-10-22 00:00:00, count=566, uniques=168),
        View(timestamp=2016-10-23 00:00:00, count=675, uniques=184),
        View(timestamp=2016-10-24 00:00:00, count=614, uniques=237)
      ]
    }

=======
======
Mark the notifications of the repository as read
------------------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.mark_notifications_as_read()
