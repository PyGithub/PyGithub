Development
===========

.. toctree::
   :maxdepth: 2

   getting-started
   testing
   openapi
   graphql

Deprecation warning
-------------------

Before removing attributes/methods, consider adding deprecation warnings instead.
The ``deprecated`` decorator adds deprecation warnings. It is provided by the standard library from Python 3.13
(``warnings.deprecated``) and by the `typing_extensions <https://pypi.org/project/typing-extensions/>`__ package
for earlier Python versions. Import it from ``github.compat``, which picks the right one:

.. code-block:: python

    from github.compat import deprecated

    @property
    @deprecated("Use core instead")
    def rate(self):
       pass

    @deprecated("Deprecated in favor of the new branch protection")
    def get_protected_branch(self):
       pass
