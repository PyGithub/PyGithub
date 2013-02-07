Introduction
============

PyGithub is a Python (2 and 3) library to use the `Github API v3 <http://developer.github.com/v3>`_.
With it, you can manage your `Github <http://github.com>`_ resources (repositories, user profiles, organizations, etc.) from Python scripts.

Should you have any question, any remark, or if you find a bug,
or if there is something you can do with the API but not with PyGithub,
please `open an issue <https://github.com/jacquev6/PyGithub/issues>`_.

(Very short) tutorial
---------------------

First create a Github instance::

    from github import Github

    g = Github( "user", "password" )

Then play with your Github objects::

    for repo in g.get_user().get_repos():
        print repo.name
        repo.edit( has_wiki = False )

Download and install
--------------------

This package is in the `Python Package Index <http://pypi.python.org/pypi/PyGithub>`_,
so ``easy_install PyGithub`` or ``pip install PyGithub`` should be enough.
You can also clone it on `Github <http://github.com/jacquev6/PyGithub>`_.

Licensing
---------

PyGithub is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by `GNU <http://www.gnu.org/licenses/gpl-howto.html>`_.

What next?
----------

You need to use a Github API and wonder which class implements it? `Reference of APIs <todo internal link>`_

You want all the details about PyGithub classes? `Reference of classes <todo internal link>`_
