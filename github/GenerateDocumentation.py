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
    print generateDocumentation()
