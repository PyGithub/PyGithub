#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
# ##############################################################################

import os
import fnmatch
import glob

# @todo Check links from our doc to Github API v3 ref
# - in the description of each class
# - in each ":calls:" section


def parseReference():
    badlyNamedUrls = {
        ("/gitignore/templates/C", "GET"): ("/gitignore/templates/:name", "GET"),
        ("/notifications/threads/1/subscription", "DELETE"): ("/notifications/threads/:id/subscription", "DELETE"),
        ("/notifications/threads/1/subscription", "GET"): ("/notifications/threads/:id/subscription", "GET"),
        ("/notifications/threads/1/subscription", "PUT"): ("/notifications/threads/:id/subscription", "PUT"),
    }
    undocumentedUrls = [
        ("/hooks/:name", "GET"),  # Discovered in https://github.com/jacquev6/PyGithub/issues/196
        ("/hooks", "GET"),  # Mentioned somewhere in http://developer.github.com/v3/repos/hooks/
        ("/hub", "POST"),  # Described in content/v3/repos/hooks.md
        ("/api/status.json", "GET"),  # https://status.github.com/api
        ("/api/last-message.json", "GET"),  # https://status.github.com/api
        ("/api/messages.json", "GET"),  # https://status.github.com/api
    ]
    uninterestingUrls = [
        ("/markdown/raw", "POST"),  # Job is done by /markdown => useless in PyGithub
        ("/repos/octocat/Hello-World/git/refs/heads/feature-a", "DELETE"),  # Example of DELETE /repos/:owner/:repo/git/refs/:ref
        ("/repos/octocat/Hello-World/git/refs/tags/v1.0", "DELETE"),  # Example of DELETE /repos/:owner/:repo/git/refs/:ref
        ("/repos/:owner/:repo/git/trees/:sha?recursive=1", "GET"),  # Example of GET /repos/:owner/:repo/git/trees/:sha
        ("/repos/:owner/:repo/git/refs/heads/skunkworkz/featureA", "GET"),  # Example of GET /repos/:owner/:repo/git/refs
        ("/repos/:owner/:repo/git/refs/tags", "GET"),  # Example of GET /repos/:owner/:repo/git/refs
    ]

    urls = dict()

    for root, _, filenames in os.walk('developer.github.com'):
        for filename in fnmatch.filter(filenames, '*.md'):
            filename = os.path.join(root, filename)
            with open(filename) as f:
                for line in f:
                    if line.startswith("#"):
                        section = ("-".join(line.rstrip().split(" ")[1:]))  # ## @todo anchor-ify (lowercase, only a-z, etc.)
                    if line.startswith("    "):
                        line = line[4:]
                    if line.startswith("\t"):
                        line = line[1:]
                    for v in ["GET", "PATCH", "DELETE", "POST", "PUT"]:
                        if line.startswith(v + " /"):
                            verb, url = line.strip().split(" ")
                            url = (url, verb)
                            if url in badlyNamedUrls:
                                url = badlyNamedUrls[url]
                            docUrl = "http://developer.github.com/" + filename[29:-3]  # ## @todo + "#" + section
                            urls[url] = docUrl

    for url in undocumentedUrls:
        urls[url] = None

    for url in uninterestingUrls:
        del urls[url]

    return urls


def parseLibrary():
    urls = dict()

    for filename in glob.glob("github/*.py"):
        with open(filename) as f:
            for line in f:
                if line.startswith("        :calls:"):
                    line = line[17:-3]
                    for part in line.split("`_ or `"):
                        verb, apiUrl, docUrl = part.split(" ")
                        docUrl = docUrl[1:-1]
                        urls[(apiUrl, verb)] = docUrl

    return urls


def printUrls(title, urls):
    if len(urls) > 0:
        print len(urls), "URLs", title + ":"
        print " ", "\n  ".join(url + " (" + verb + ")" for url, verb in sorted(urls))
        print


def main():
    ref = parseReference()
    lib = parseLibrary()
    printUrls("in Github API v3, but not implemented in PyGithub", set(ref) - set(lib))
    printUrls("called by PyGithub but not existing in Github API v3", set(lib) - set(ref))
    for key in set(lib) & set(ref):
        (url, verb) = key
        if ref[key] is not None and lib[key] != ref[key] and not lib[key].startswith(ref[key] + "/#"):
            print "sed -i \"s@:calls: ." + verb + " " + url + " ." + lib[key] + ".._" + "@:calls: \\`" + verb + " " + url + " \\<" + ref[key] + "\\>\\`_@\" github/*.py"


if __name__ == "__main__":
    main()
