PyGithub
========

PyGithub is a Python library to access the full `Github API v3 <http://developer.github.com/v3>`__.
**This is the documentation of the v2**. While v2 is in alpha stage,
you may want to continue to use `v1 <http://jacquev6.github.io/PyGithub/v1>`__ .

This documentation is structured as follows:

 * A short :ref:`introduction` to start using PyGithub in a few minutes
 * A brief :ref:`migration` to help you migrate your code from v1 to v2.
 * A comprehensive :ref:`user_guide` to cover all the topics you need to use PyGithub in your project
 * A :ref:`cook_book`
 * A :ref:`rationale` to understand the choices made in the design of PyGithub
 * A thoroughly cross-linked :ref:`reference`

.. toctree::
  :hidden:

  introduction
  user_guide
  cook_book
  rationale
  reference
  migration

Migration strategy and maintenance schedule
===========================================

Alpha
-----

The Alpha phase of PyGithub v2 started on March 2nd, 2014. As of Jully 11th, we are still in the Alpha phase. During this phase:

 * You should continue to use v1 for your projects: I will continue to maintain v1, investigate and fix bugs and accept pull requests for new features but I won't spend time implementing new features.
 * You can use v2 if you want to have a preview or if you want to contribute to its development. v2 will be unstable: its API and behavior can change without any restriction. Development of v2 happens in branch `develop_v2 <https://github.com/jacquev6/PyGithub/tree/develop_v2>`__. Versions are taged v2.0.0-alpha.N where N is a simple integer.
 * I'm not publishing v2 on PyPI, you have to clone it from GitHub.

Beta
----

The Beta phase will start when I publish the first package for v2 on PyPI (v2.0.0-beta.1). During this phase:

 * You should use v2 in your projects if you can tolerate small changes. API and behavior should be stable and will change only to fix bugs and unintuitive things.
 * I will create a branch master_v2 pointing to the code of last beta package published, while development goes on in branch develop_v2.

Stable
------

After the release of the first stable v2 (v2.0.0):

 * You should use v2 for your new projects and migrate your existing projects to v2.
 * I will maintain v1 for 3 months (only to investigate and fix bugs).
 * v1 will be maintained in branch master_v1, and the branches master and develop will be hard-reset to their corresponding _v2.

Then after 3 months I will stop maintaining v1. Branch master_v1 and associated tags will stay in the git repository for archive purpose only.
