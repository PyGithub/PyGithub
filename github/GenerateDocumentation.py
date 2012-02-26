#!/bin/env python

import GithubObject
import GithubObjects

def generateDocumentation():
    classes = [ getattr( GithubObjects, c ) for c in dir( GithubObjects ) if hasattr( getattr( GithubObjects, c ), "_autoDocument" ) ]
    doc = ""
    for c in classes:
        doc += c._autoDocument()
    return doc

if __name__ == "__main__":
    print """\
You don't normaly create instances of any class but `Github`.
You obtain instances through calls to `get_` and `create_` methods.

In this documentation:

* `login` is a string containing a user's or organization's login
* `user` is an instance of `AuthenticatedUser` or `NamedUser`
* `name` is a string containing the name of a repository
* `repo` is an instance of `Repository`

Class `Github`
==============
* Constructed from user's login and password
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`
"""
    print generateDocumentation()
