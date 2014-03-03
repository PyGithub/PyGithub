.. _migration:

Migration guide
===============

This migration guide may look a bit terse. I will update it with your questions,
don't hesitate to `open an issue <https://github.com/jacquev6/PyGithub/issues/new>`_.

The main difference between v1 and v2 is how you build the :class:`.Github` instance:
in v2, you ``import PyGithub`` and then configure it using the :class:`.Builder` as described in :ref:`configuration`.

Another difference is that in :class:`.Github`, there are now two different methods to acces the authenticated user
(:meth:`.Github.get_authenticated_user`) and another user by its login (:meth:`.Github.get_user`).

Globally, the other methods look like v1, but accept more types of input: you can always substitute an identifier for an object,
where in v1 you had to pass a Github object like Repository or User.
