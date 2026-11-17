Getting started
===============

Source code
-----------

This project's sources can be found at Github: https://github.com/PyGithub/PyGithub

Coding style
------------

PyGithub adopts the `ruff <https://docs.astral.sh/ruff/>`__ coding style, using ruff for linting and formatting.

To manually format the code::

    pre-commit run --all-files --show-diff-on-failure
    mypy github tests

If you use tox::

    tox -e lint

Pre-commit plugin
-----------------

To forget about coding style and let `pre-commit <https://pre-commit.com/#installation>`__ fix your ruff issues::

    pre-commit install

That's it!

Build documentation locally
---------------------------

You can build the documentation with Sphinx::

    pip install -r requirements/docs.txt
    sphinx-build doc build

If you use tox::

    tox -edocs
