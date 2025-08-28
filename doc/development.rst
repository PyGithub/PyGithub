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
