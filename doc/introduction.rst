Introduction
============

PyGithub is a Python (2 and 3) library to use the `Github API v3 <http://developer.github.com/v3>`__.
With it, you can manage your `Github <http://github.com>`__ resources (repositories, user profiles, organizations, etc.) from Python scripts.

Should you have any question, any remark, or if you find a bug,
or if there is something you can do with the API but not with PyGithub,
please `open an issue <https://github.com/jacquev6/PyGithub/issues>`__.

(Very short) tutorial
---------------------

First create a Github instance::

    from github import Github

    g = Github("user", "password")

Then play with your Github objects::

    for repo in g.get_user().get_repos():
        print repo.name
        repo.edit(has_wiki=False)

Download and install
--------------------

This package is in the `Python Package Index <http://pypi.python.org/pypi/PyGithub>`__,
so ``easy_install PyGithub`` or ``pip install PyGithub`` should be enough.
You can also clone it on `Github <http://github.com/jacquev6/PyGithub>`__.

Licensing
---------

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by `GNU <http://www.gnu.org/licenses/gpl-howto.html>`__.

What next?
----------

You need to use a Github API and wonder which class implements it? [`Reference of APIs`](http://jacquev6.net/PyGithub/v1/apis.html) __

You want all the details about PyGithub classes? [`Reference of classes`](http://jacquev6.net/PyGithub/v1/github_objects.html) __

Projects using PyGithub
-----------------------

(`Open an issue <https://github.com/jacquev6/PyGithub/issues>`__ if you want to be listed here, I'll be glad to add your project)

* `Github-iCalendar <http://danielpocock.com/github-issues-as-an-icalendar-feed>`__ returns all of your Github issues and pull requests as a list of tasks / VTODO items in iCalendar format.
* `DevAssistant <http://devassistant.org>`_
* `Upverter <https://upverter.com>`__ is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Github project to an Upverter project.
* `Notifico <http://n.tkte.ch>`__ receives messages (such as commits and issues) from services and scripts and delivers them to IRC channels. It can import/sync from Github.
* `Tratihubis <http://pypi.python.org/pypi/tratihubis/>`__ converts Trac tickets to Github issues
* https://github.com/CMB/cligh
* https://github.com/natduca/quickopen uses PyGithub to automaticaly create issues
* https://gist.github.com/3433798
* https://github.com/zsiciarz/aquila-dsp.org
* https://github.com/robcowie/virtualenvwrapper.github
* https://github.com/kokosing/git-gifi - Git and github enhancements to git.

They talk about PyGithub
------------------------

* http://stackoverflow.com/questions/10625190/most-suitable-python-library-for-github-api-v3
* http://stackoverflow.com/questions/12379637/django-social-auth-github-authentication
* http://www.freebsd.org/cgi/cvsweb.cgi/ports/devel/py-pygithub/
* https://bugzilla.redhat.com/show_bug.cgi?id=910565
