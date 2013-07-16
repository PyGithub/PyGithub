#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import fnmatch
import glob

# @todo Check links from our doc to Github API v3 ref
# - in the description of each class
# - in each ":calls:" section


def parseReference():
    badlyNamedUrls = {
        "/gitignore/templates/C GET": "/gitignore/templates/:name GET",
        "/notifications/threads/1/subscription DELETE": "/notifications/threads/:id/subscription DELETE",
        "/notifications/threads/1/subscription GET": "/notifications/threads/:id/subscription GET",
        "/notifications/threads/1/subscription PUT": "/notifications/threads/:id/subscription PUT",
    }
    undocumentedUrls = [
        "/hooks GET",  # Mentioned somewhere
        "/hub POST",  # Described in content/v3/repos/hooks.md
    ]
    uninterestingUrls = [
        "/markdown/raw POST",  # Job is done by /markdown => useless in PyGithub
        "/repos/octocat/Hello-World/git/refs/heads/feature-a DELETE",  # Example of DELETE /repos/:owner/:repo/git/refs/:ref
        "/repos/octocat/Hello-World/git/refs/tags/v1.0 DELETE",  # Example of DELETE /repos/:owner/:repo/git/refs/:ref
        "/repos/:owner/:repo/git/trees/:sha?recursive=1 GET",  # Example of GET /repos/:owner/:repo/git/trees/:sha
        "/repos/:owner/:repo/git/refs/heads/skunkworkz/featureA GET",  # Example of GET /repos/:owner/:repo/git/refs
        "/repos/:owner/:repo/git/refs/tags GET",  # Example of GET /repos/:owner/:repo/git/refs
    ]

    urls = set()

    for root, _, filenames in os.walk('developer.github.com'):
        for filename in fnmatch.filter(filenames, '*.md'):
            filename = os.path.join(root, filename)
            with open(filename) as f:
                for line in f:
                    if line.startswith("    "):
                        line = line[4:]
                    if line.startswith("\t"):
                        line = line[1:]
                    for v in ["GET", "PATCH", "DELETE", "POST", "PUT"]:
                        if line.startswith(v + " /"):
                            verb, url = line.strip().split(" ")
                            url = url + " " + verb
                            if url in badlyNamedUrls:
                                url = badlyNamedUrls[url]
                            urls.add(url)

    for url in undocumentedUrls:
        urls.add(url)

    for url in uninterestingUrls:
        urls.remove(url)

    return urls


def parseLibrary():
    urls = set()

    for filename in glob.glob("github/*.py"):
        with open(filename) as f:
            for line in f:
                if line.startswith("        :calls:"):
                    line = line[17:-3]
                    for part in line.split("`_ or `"):
                        verb, url, _ = part.split(" ")
                        urls.add(url + " " + verb)

    return urls


def parseApiList():
    urls = set()

    with open("doc/apis.rst") as f:
        url = None
        for line in f:
            if line.startswith("*"):
                newUrl = line[4:-3]
                if url is not None:
                    assert newUrl > url, url
                url = newUrl
            elif line.startswith("  * "):
                verb = line[4:].split(":")[0]
                if "Not implemented" not in line:
                    urls.add(url + " " + verb)

    return urls


def printUrls(title, urls):
    if len(urls) > 0:
        print len(urls), "URLs", title + ":"
        print " ", "\n  ".join(sorted(urls))
        print


def main():
    ref = parseReference()
    lib = parseLibrary()
    doc = parseApiList()
    printUrls("in Github API v3, but not implemented in PyGithub", ref - lib)
    printUrls("called by PyGithub but not existing in Github API v3", lib - ref)
    printUrls("badly linked from doc/api.rst", doc ^ lib)


if __name__ == "__main__":
    main()
