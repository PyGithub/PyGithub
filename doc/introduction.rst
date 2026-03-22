Introduction
============

PyGithub is a Python library to use the `Github API v3 <http://developer.github.com/v3>`__.
With it, you can manage your `Github <http://github.com>`__ resources (repositories, user profiles, organizations, etc.) from Python scripts.

Should you have any question, any remark, or if you find a bug,
or if there is something you can do with the API but not with PyGithub,
please `open an issue <https://github.com/PyGithub/PyGithub/issues>`__.

(Very short) tutorial
---------------

.. tabs::

    .. tab:: Sync

        First create a Github instance:

        .. code-block:: python

            from github import Github, Auth

            auth = Auth.Token("access_token")

            # Public Web Github
            g = Github(auth=auth)

            # Github Enterprise with custom hostname
            g = Github(auth=auth, base_url="https://{hostname}/api/v3")

        Then play with your Github objects:

        .. code-block:: python

            for repo in g.get_user().get_repos():
                print(repo.name)
                repo.edit(has_wiki=False)
                # to see all the available attributes and methods
                print(dir(repo))

        To close connections after use:

        .. code-block:: python

            g.close()

    .. tab:: Async

        First create a Github instance:

        .. code-block:: python

            import asyncio
            from github.asyncio import Github
            from github import Auth

            auth = Auth.Token("access_token")

            async def main():
                # Public Web Github
                g = Github(auth=auth)

                # Github Enterprise with custom hostname
                g = Github(auth=auth, base_url="https://{hostname}/api/v3")

        Then play with your Github objects -- methods that hit the API and properties
        that trigger lazy-loading must be ``await``-ed:

        .. code-block:: python

                async for repo in (await g.get_user()).get_repos():
                    print(await repo.name)
                    await repo.edit(has_wiki=False)
                    print(dir(repo))

        To close connections after use:

        .. code-block:: python

                await g.close()

            asyncio.run(main())

        See :doc:`async` for a full explanation of what becomes awaitable.

Download and install
--------------------

This package is in the `Python Package Index
<http://pypi.python.org/pypi/PyGithub>`__, so ``pip install PyGithub`` should
be enough.  You can also clone it on `Github
<http://github.com/PyGithub/PyGithub>`__.

Licensing
---------

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by `GNU <http://www.gnu.org/licenses/gpl-howto.html>`__.

What next?
----------

You need to use a Github API and wonder which class implements it? `Reference of APIs <https://pygithub.readthedocs.io/en/latest/apis.html>`__.

Contributing
------------

This project is community-driven. New PyGithub classes, methods and fixes are authored by the community, then reviewed and released by the project maintainers.

See our :doc:`development` guide for further details.

Sponsoring
----------

Please consider sponsoring this project. Look out for the "Sponsor this project" area on the `PyGithub project page <https://github.com/PyGithub/PyGithub>`__.

Projects using PyGithub
-----------------------

(`Open an issue <https://github.com/PyGithub/PyGithub/issues>`__ if you want to be listed here, I'll be glad to add your project)

* `Github-iCalendar <http://danielpocock.com/github-issues-as-an-icalendar-feed>`__ returns all of your Github issues and pull requests as a list of tasks / VTODO items in iCalendar format.
* `DevAssistant <http://devassistant.org>`_
* `Upverter <https://upverter.com>`__ is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Github project to an Upverter project.
* `Notifico <http://n.tkte.ch>`__ receives messages (such as commits and issues) from services and scripts and delivers them to IRC channels. It can import/sync from Github.
* `Tratihubis <http://pypi.python.org/pypi/tratihubis/>`__ converts Trac tickets to Github issues
* https://github.com/fga-gpp-mds/2018.1-Cardinals - website that shows metrics for any public repository (issues, commits, pull requests etc)
* https://github.com/CMB/cligh
* https://github.com/natduca/quickopen uses PyGithub to automatically create issues
* https://gist.github.com/3433798
* https://github.com/zsiciarz/aquila-dsp.org
* https://github.com/robcowie/virtualenvwrapper.github
* https://github.com/kokosing/git-gifi - Git and github enhancements to git.
* https://github.com/csurfer/gitsuggest - A tool to suggest github repositories based on the repositories you have shown interest in
* https://github.com/gomesfernanda/some-github-metrics - Python functions for relevant metrics on GitHub repositories
* https://github.com/SOM-Research/Gitana - a SQL-based Project Activity Inspector
* https://github.com/plus3it/satsuki - Automate GitHub releases and uploading binary release assets
* `check-in <https://github.com/webknjaz/check-in>`_ — Python CLI distribution that allows user to use GitHub Checks API as a bot.
* https://github.com/hasii2011/gittodoistclone - Convert GitHub issues to Todoist tasks

They talk about PyGithub
------------------------

* http://stackoverflow.com/questions/10625190/most-suitable-python-library-for-github-api-v3
* http://stackoverflow.com/questions/12379637/django-social-auth-github-authentication
* http://www.freebsd.org/cgi/cvsweb.cgi/ports/devel/py-pygithub/
* https://bugzilla.redhat.com/show_bug.cgi?id=910565
