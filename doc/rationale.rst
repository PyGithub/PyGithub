.. _rationale:

Rationale
=========

Please note this section is in progress. I'll be happy to give you more explainations if you want.
`Open an issue <https://github.com/jacquev6/PyGithub/issues/new>`_.

Raise late on bad attributes
----------------------------

If GitHub returns an unexpected type for an attribute, PyGithub will raise an exception only when you access the attribute.
This means the user is impacted only by errors in the data he uses.

Generate the code
-----------------

The biggest challenge in maintaining PyGithub v1 was the amount of very similar code.
For v2, I've decided to generate all the repeated code from a structured description of the GitHub Api v3.

Another approach would have been to write meta-code that generates needed classe on the fly, but documenting and debuging such
code is a nightmare. By generating the code, I'm able to experiment with manual code and modify the generator only when it's validated.

Commiting the generated code allows me to review all changes and makes it easy for people to look into the real code.

Naming conventions
------------------

* Lower case separated by underscores for method and attributes mapping directly to GitHub API v3
* Pascal case for method and attributes specific to PyGithub.

The package itself has been renamed `PyGithub` to make it obvious that it's installed by ``pip install PyGithub``.

:meth:`delete` does not invalidate the object
---------------------------------------------

Nothing is done to prevent you from using an object after a call to its :meth:`delete` method. Just don't.
This way, you're free to use the properties of a deleted object if you want.
