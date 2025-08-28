Getting started
===============

Source code
-----------

This project's sources can be found at Github: https://github.com/PyGithub/PyGithub

Coding style
------------

PyGithub adopts the black coding style.

To manually format the code::

    tox -e lint

Pre-commit plugin
-----------------

To forget about coding style and let `pre-commit <https://pre-commit.com/#installation>`__ fix your flake8/isort/black issue::

    pre-commit install

That's it!

Deprecation warning
-------------------

Before removing attributes/methods, consider adding deprecation warnings instead.
The `typing_extensions <https://pypi.org/project/typing-extensions/>`__ package provides a handy decorator to add deprecation warnings.

.. code-block:: python

    from typing_extensions import deprecated

    @property
    @deprecated("Use core instead")
    def rate(self):
       pass

    @deprecated("Deprecated in favor of the new branch protection")
    def get_protected_branch(self):
       pass


Build documentation locally
---------------------------

You can build the documentation with Sphinx::

    pip install -r requirements/docs.txt
    sphinx-build doc build

If you use tox::

    tox -edocs
