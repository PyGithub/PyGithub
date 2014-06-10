#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import fnmatch
import glob
import os
import re
import sys


class EndPoint:
    def __init__(self, verb, url, doc):
        self.verb = verb
        self.url = url
        self.doc = doc
        self.params = []


class Section:
    def __init__(self, name, lines, level):
        self.name = name
        self.lines = lines
        self.level = level
        self.intro = []

        subsections = []
        current = self.intro
        for line in lines:
            if line.startswith(level * "#" + " "):
                title = line[level + 1:]
                current = []
                subsections.append((title, current))
            else:
                current.append(line)
        assert len(self.intro) + sum(len(s[1]) + 1 for s in subsections) == len(lines)

        self.sections = [
            Section(n, l, level + 1) for n, l in subsections
        ]

    def printStructure(self, level=0):
        print 2 * level * " " + self.name
        for s in self.sections:
            s.printStructure(level + 1)


class File(Section):
    def __init__(self, name):
        with open(name) as f:
            Section.__init__(self, name, [l.rstrip() for l in f], 1)


class Param:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class ReferenceDocumentation:
    badlyNamedUrls = {
        "/gitignore/templates/C": "/gitignore/templates/:name",
    }
    uninterestingUrls = [
        "/markdown/raw",  # Job is done by /markdown => useless in PyGithub
        "/repos/octocat/Hello-World/git/refs/heads/feature-a",  # Example of DELETE /repos/:owner/:repo/git/refs/:ref
        "/repos/octocat/Hello-World/git/refs/tags/v1.0",  # Example of DELETE /repos/:owner/:repo/git/refs/:ref
        "/repos/:owner/:repo/git/trees/:sha?recursive=1",  # Example of GET /repos/:owner/:repo/git/trees/:sha
        "/repos/:owner/:repo/git/refs/heads/skunkworkz/featureA",  # Example of GET /repos/:owner/:repo/git/refs
        "/repos/:owner/:repo/git/refs/tags",  # Example of GET /repos/:owner/:repo/git/refs
        "/repos/octokit/octokit.rb",  # Example
        "/orgs/octokit/repos",  # Example
        "/users/:user/watched",  # Legacy
        "/user/watched",  # Legacy
        "/user/watched/:owner/:repo",  # Legacy
        "/repos/:owner/:repo/watchers",  # Legacy
        "/legacy/issues/search/:owner/:repository/:state/:keyword",  # Legacy
        "/legacy/repos/search/:keyword",  # Legacy
        "/legacy/user/email/:email",  # Legacy
        "/legacy/user/search/:keyword",  # Legacy
    ]

    def __init__(self, rootDirectory):
        self.rootDirectory = rootDirectory
        self.endPoints = []
        self.files = []

        self.readFiles()
        self.analyseFiles()

        self.endPoints.append(EndPoint("GET", "/hooks", "http://developer.github.com/v3/repos/hooks"))
        self.endPoints.append(EndPoint("GET", "/hooks/:name", "https://github.com/jacquev6/PyGithub/issues/196"))
        self.endPoints.append(EndPoint("POST", "/hub", "http://developer.github.com/v3/repos/hooks#pubsubhubbub"))
        self.endPoints.append(EndPoint("GET", "/api/status.json", "https://status.github.com/api"))
        self.endPoints.append(EndPoint("GET", "/api/last-message.json", "https://status.github.com/api"))
        self.endPoints.append(EndPoint("GET", "/api/messages.json", "https://status.github.com/api"))

    def readFiles(self):
        for root, _, fileNames in os.walk(self.rootDirectory):
            if not root.endswith("content/changes"):
                for fileName in fnmatch.filter(fileNames, '*.md'):
                    fileName = os.path.join(root, fileName)
                    file = File(fileName)
                    self.files.append(file)

    def analyseFiles(self):
        for f in self.files:
            self.analyseFile(f)

    def analyseFile(self, f):
        docBase = "http://developer.github.com/" + f.name[32:-3]
        self.findEndPoints_rec([f], docBase, "")

    def findEndPoints_rec(self, parents, docBase, anchor):
        section = parents[-1]
        endPoints = self.findEndPoints(section.intro, docBase + anchor)
        self.endPoints += endPoints
        if len(endPoints) == 0:
            for sub in section.sections:
                m = re.match(".* {#(.*)}", sub.name)
                if m:
                    anchor = m.group(1)
                else:
                    anchor = sub.name
                anchor = anchor.lower().replace(" ", "-").translate(None, "#()&;'`,\"?./*:[]")
                for c in anchor:
                    assert c in "abcdefghijklmnopqrstuvwxyz-0123456789", ("Delete bad chars in", anchor)
                self.findEndPoints_rec(parents + [sub], docBase, "#" + anchor)
        else:
            params = []
            for sub in section.sections:
                for ss in sub.sections:
                    if ss.name != "Example":
                        self.warning("check that section", " -> ".join(s.name for s in parents), "->", sub.name, "->", ss.name, "is empty")
                if any(sub.name.startswith(prefix) for prefix in ["Parameter", "Optional Parameters", "Input", "Alternative Input"]):
                    params += self.findParams(sub.intro)
                elif "Response" in sub.name or "response" in sub.name:
                    pass
                else:
                    self.warning("don't know what to do with section", " -> ".join(s.name for s in parents), "->", sub.name)
            for ep in endPoints:
                ep.params = params

    def findEndPoints(self, lines, doc):
        endPoints = []
        for line in lines:
            if line.startswith("    "):
                line = line[4:]
            if line.startswith("\t"):
                line = line[1:]
            for v in ["GET", "PATCH", "DELETE", "POST", "PUT"]:
                if line.startswith(v + " /"):
                    parts = line.split(" ")
                    if len(parts) == 2:
                        verb, url = parts
                        if url in self.badlyNamedUrls:
                            url = self.badlyNamedUrls[url]
                        if url not in self.uninterestingUrls:
                            endPoints.append(EndPoint(verb, url, doc))
                    else:
                        self.warning("Strange line", line)
        return endPoints

    def findParams(self, lines):
        params = []
        for line in lines:
            if line == "":
                continue
            if line.startswith("<%= "):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) == 3:
                name, type, description = parts
                if name == "Name" and type == "Type" and description == "Description":
                    continue
                if name.startswith("-----"):
                    continue
                param = Param(name.strip("`"), type)
                params.append(param)
            # else:
            #     self.warning("Strange line", line)
        return params

    def warning(self, *texts):
        text = "WARNING: " + " ".join(texts)
        if text not in [
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/git/commits.md -> Commits -> Create a Commit -> Example Input",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/git/tags.md -> Tags -> Create a Tag Object -> Example Input",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/orgs.md -> Organizations -> Edit an Organization -> Example",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/pulls.md -> Pull Requests -> Get a single pull request -> Mergability",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/repos.md -> Repositories -> Create -> OAuth scope requirements",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/repos/commits.md -> Commits -> Compare two commits -> Working with large comparisons",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/repos/contents.md -> Contents -> Create a file -> Example Input",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/repos/contents.md -> Contents -> Delete a file -> Example Input",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/repos/contents.md -> Contents -> Update a file -> Example Input",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/search.md -> Search -> Search code -> Highlighting Code Search Results",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/search.md -> Search -> Search issues -> Highlighting Issue Search Results",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/search.md -> Search -> Search repositories -> Highlighting Repository Search Results",
            "WARNING: don't know what to do with section ../developer.github.com/content/v3/search.md -> Search -> Search users -> Highlighting User Search Results",

            "WARNING: check that section ../developer.github.com/content/v3/rate_limit.md -> Rate Limit -> Get your current rate limit status -> Response -> Deprecation Notice is empty",
            "WARNING: check that section ../developer.github.com/content/v3/rate_limit.md -> Rate Limit -> Get your current rate limit status -> Response -> Understanding Your Rate Limit Status is empty",

            "WARNING: Strange line POST /payload HTTP/1.1",
        ]:
            print text


def main():
    ref = ReferenceDocumentation("../developer.github.com")

    endPoints = {}
    for endPoint in ref.endPoints:
        if endPoint.url not in endPoints:
            endPoints[endPoint.url] = {}
        endPoints[endPoint.url][endPoint.verb] = ([p.name for p in endPoint.params], endPoint.doc)

    with open(os.path.join("ApiDefinition", "end_points.yml"), "w") as f:
        for url, ops in sorted(endPoints.iteritems()):
            f.write(url + ":\n")
            for verb, [params, doc] in sorted(ops.iteritems()):
                f.write("  - verb: " + verb + "\n")
                if len(params) != 0:
                    f.write("    parameters: [" + ", ".join(sorted(params)) + "]\n")
                f.write("    doc: " + doc + "\n")


if __name__ == "__main__":
    main()
