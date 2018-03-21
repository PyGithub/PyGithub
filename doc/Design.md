Typology of URLs
================

Object URLs
-----------

They

 - return a single object on GET
 - may be PATCH-able (to modify the object)
 - may be DELETE-able (to... delete the object)

List URLs
---------

They

 - return a list of objects on GET (some of them are not GET-able)
 - may be POST-able (to create a new object)
 - may have specific URLs for their elements, that
   - may be PUT-able (to add an existing object to this list)
   - may be GET-able (to ask if an object is in the list)
   - may be DELETE-able (to remove an object from the list)

Laziness
========

An URL returning a list of objects returns most of the information
about its elements, but not all. So, we have a lazy completion for
objects returned by the API: we do a GET on their object URL when
the user asks an attribute we have not got from the list of objects.

We don't use lazy completion for objects requested by name by user,
to detect name errors as soon as possible.

Attributes vs. methods
======================

We have methods for API calls, and attributes for in-memory reads
(except for lazy attributes that may trigger a call to an URL).
Methods are named with a verb prefix to avoid name clashes with attributes.
(`followers` is an attribute of User giving the number of followers,
and `get_followers` is a method returning the list of followers)

Explicit `edit` methods
=======================

To modify objects, we have a single `edit` method (not several
writable attributes) to be explicit about API calls.

Typology of attributes
======================
* Internality
	* Internal (received in the GET request about this object) => attribute (lazy completion if needed)
	* External (needs another new GET request) => method
* Type
	* Simple type
	* GithubObject
	* List of simple type
	* List of GithubObject
	* Dict of...
