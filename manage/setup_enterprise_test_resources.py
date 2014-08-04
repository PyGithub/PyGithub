#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import sys
sys.path.append(".")
import time

import PyGithub


def ensure(o, **attrs):
    if any(getattr(o, k) != v for k, v in attrs.iteritems()):
        print "Reset", o, "to", attrs
        o.edit(**{k: (PyGithub.Blocking.Reset if v is None else v) for k, v in attrs.iteritems()})
        verify(o, **attrs)


def verify(o, **attrs):
    assert all(getattr(o, k) == v for k, v in attrs.iteritems())


b = PyGithub.BlockingBuilder().Enterprise("github.home.jacquev6.net")
gZeus = b.Login("zeus", "password1-zeus").Build()
gPoseidon = b.Login("poseidon", "password1-poseidon").Build()
gAntigone = b.Login("antigone", "password1-antigone").Build()
gElectra = b.Login("electra", "password1-electra").Build()
gPenelope = b.Login("penelope", "password1-penelope").Build()

# There is no API to create users, so we need to create them manually
zeus = gZeus.get_authenticated_user()
verify(zeus, site_admin=True, suspended_at=None)
ensure(zeus, name="Zeus, god of the sky", email="ghe-zeus@jacquev6.net", location="High in the sky", blog="http://jacquev6.net/zeus", hireable=False, company="Zeus Software")

poseidon = gPoseidon.get_authenticated_user()
verify(poseidon, site_admin=True, suspended_at=None)
ensure(poseidon, name="Poseidon, god of the sea", email="ghe-poseidon@jacquev6.net", location="Deep in the sea", blog="http://jacquev6.net/poseidon", hireable=False, company="Poseidon Software")

assert b.Build().get_user("morpheus").suspended_at

# Do not modify: antigone.updated_at is tested
antigone = gAntigone.get_authenticated_user()
verify(antigone, site_admin=False, suspended_at=None)
ensure(antigone, name="Antigone", email="ghe-antigone@jacquev6.net", location="Greece", blog="http://jacquev6.net/antigone", hireable=False, company="Antigone Software")

electra = gElectra.get_authenticated_user()
verify(electra, site_admin=False, suspended_at=None)
ensure(electra, name="Electra", email="ghe-electra@jacquev6.net", location="Greece", blog="http://jacquev6.net/electra", hireable=False, company="Electra Software")

# Modify freely: no test assert anything about this user
penelope = gPenelope.get_authenticated_user()
verify(penelope, site_admin=False, suspended_at=None)
ensure(penelope, name=None, email=None, location=None, blog=None, hireable=False, company=None)


underground = gZeus.get_org("underground")
ensure(underground, billing_email="ghe-underground@jacquev6.net", blog=None, company=None, email=None, location=None, name=None)

olympus = gZeus.get_org("olympus")
ensure(olympus, billing_email="ghe-olympus@jacquev6.net", blog=None, company=None, email=None, location=None, name=None)

for m in olympus.get_members():
    if m.login != "zeus":
        olympus.remove_from_members(m)
for t in olympus.get_teams():
    if t.name != "Owners":
        t.delete()
gods = olympus.create_team("Gods", permission="admin")
gods.add_to_members("poseidon")
gods.add_to_members("zeus")
humans = olympus.create_team("Humans", permission="push")
humans.add_to_members("antigone")
humans.add_to_members("electra")
gZeus.get_org("olympus").add_to_public_members("zeus")
gPoseidon.get_org("olympus").add_to_public_members("poseidon")
gAntigone.get_org("olympus").add_to_public_members("antigone")


electra.add_to_following("zeus")
electra.add_to_following("poseidon")
poseidon.add_to_following("zeus")


try:
    # gElectra.get_repo(("electra", "issues")).delete()
    gElectra.get_repo(("electra", "issues"))
except PyGithub.Blocking.ObjectNotFoundException:
    time.sleep(5)
    r = gElectra.get_authenticated_user().create_repo("issues", auto_init=True)
    time.sleep(5)
    r.create_milestone("Immutable milestone")
    r.create_milestone("Closed milestone", state="closed")
    r.create_milestone("Mutable milestone")
    gPenelope.get_repo(("electra", "issues")).create_issue("Immutable issue")
    gPenelope.get_repo(("electra", "issues")).create_issue("Closed issue 1", body="@electra")
    gPenelope.get_repo(("electra", "issues")).create_issue("Closed issue 2", body="@electra")
    gPenelope.get_repo(("electra", "issues")).create_issue("Mutable issue")
    r.get_issue(1).edit(assignee="electra", labels=["enhancement", "question"])
    r.get_issue(2).edit(assignee="electra", labels=["enhancement", "question"], state="closed", milestone=1)
    r.get_issue(3).edit(assignee="electra", labels=["enhancement", "question"], state="closed", milestone=1)
    r.add_to_collaborators("penelope")

try:
    # gElectra.get_repo(("electra", "pulls")).delete()
    # gPenelope.get_repo(("penelope", "pulls")).delete()
    gElectra.get_repo(("electra", "pulls"))
    gPenelope.get_repo(("penelope", "pulls"))
except PyGithub.Blocking.ObjectNotFoundException:
    time.sleep(5)
    source = gElectra.get_authenticated_user().create_repo("pulls", auto_init=True)
    time.sleep(5)
    source.create_milestone("First milestone")
    fork = gPenelope.get_authenticated_user().create_fork(("electra", "pulls"))
    time.sleep(5)
    source.create_file("conflict.md", "Create conflict.md", "Zm9v")
    master = fork.get_git_ref("refs/heads/master").object.sha
    fork.create_git_ref("refs/heads/merged", master)
    fork.create_git_ref("refs/heads/mergeable", master)
    fork.create_git_ref("refs/heads/issue_to_pull", master)
    fork.create_git_ref("refs/heads/conflict", master)
    fork.create_git_ref("refs/heads/mutable", master)
    fork.create_file("merged.md", "Create merged.md", "bWVyZ2U=", branch="merged")
    fork.create_file("mergeable.md", "Create mergeable.md", "bWVyZ2U=", branch="mergeable")
    fork.create_file("issue_to_pull.md", "Create issue_to_pull.md", "bWVyZ2U=", branch="issue_to_pull")
    fork.create_file("conflict.md", "Create conflict.md", "YmFy", branch="conflict")
    fork.create_file("mutable.md", "Create mutable.md", "YmFy", branch="mutable")
    sourceForPenelope = gPenelope.get_repo(("electra", "pulls"))
    sourceForPenelope.create_pull("Merged pull", "penelope:merged", "master")
    sourceForPenelope.create_pull("Mergeable pull", "penelope:mergeable", "master")
    sourceForPenelope.create_pull("Conflict pull", "penelope:conflict", "master")
    sourceForPenelope.create_pull("Mutable pull", "penelope:mutable", "master")
    source.get_pull(1).merge()


try:
    # gElectra.get_repo(("electra", "immutable")).delete()
    gElectra.get_repo(("electra", "immutable"))
except PyGithub.Blocking.ObjectNotFoundException:
    time.sleep(5)
    gElectra.get_authenticated_user().create_repo("immutable", auto_init=True)
    time.sleep(5)
    gZeus.get_org("olympus").create_fork(("electra", "immutable"))
    time.sleep(5)
    gPenelope.get_authenticated_user().create_fork(("olympus", "immutable"))
    time.sleep(5)

try:
    # gElectra.get_repo(("electra", "mutable")).delete()
    gElectra.get_repo(("electra", "mutable"))
except PyGithub.Blocking.ObjectNotFoundException:
    time.sleep(5)
    r = gElectra.get_authenticated_user().create_repo("mutable", auto_init=True)
    time.sleep(5)
    r.add_to_collaborators("penelope")
    r.add_to_collaborators("zeus")
    r.create_git_ref("refs/heads/develop", r.get_git_ref("refs/heads/master").object.sha)
    r.create_milestone("First milestone")

try:
    # gElectra.get_repo(("electra", "contributors")).delete()
    gElectra.get_repo(("electra", "contributors"))
except PyGithub.Blocking.ObjectNotFoundException:
    time.sleep(5)
    r = gElectra.get_authenticated_user().create_repo("contributors", auto_init=True)
    time.sleep(5)
    r.create_file("zeus.md", "Create zeus.md", "YmFy", author=dict(name="Zeus", email="ghe-zeus@jacquev6.net"))
    r.create_file("penelope.md", "Create penelope.md", "YmFy", author=dict(name="Penelope", email="ghe-penelope@jacquev6.net"))
    r.create_file("oedipus.md", "Create oedipus.md", "YmFy", author=dict(name="Oedipus", email="ghe-oedipus@jacquev6.net"))

try:
    gElectra.get_repo(("electra", "git-objects")).delete()
    gElectra.get_repo(("electra", "git-objects"))
except PyGithub.Blocking.ObjectNotFoundException:
    time.sleep(5)
    r = gElectra.get_authenticated_user().create_repo("git-objects", auto_init=True)
    time.sleep(5)
    r.create_file("foo.md", "Create foo.md", "bWVyZ2U=")
    r.get_readme().edit("Modify README.md", "TmV3IHJlYWRtZQ0K")
    r.create_git_ref("refs/heads/develop", r.get_git_ref("refs/heads/master").object.sha)
    r.create_git_ref("refs/tags/light-tag-1", r.get_git_ref("refs/heads/master").object.sha)
    r.create_file("bar.md", "Create bar.md", "bWVyZ2U=", branch="develop")
    r.create_git_ref("refs/tags/light-tag-2", r.get_git_ref("refs/heads/develop").object.sha)

    r.create_git_blob("This is some content", "utf8")
    # blob: 3daf0da6bca38181ab52610dd6af6e92f1a5469d
    r.create_git_tree(tree=[{"path": "test.txt", "mode": "100644", "type": "blob", "sha": "3daf0da6bca38181ab52610dd6af6e92f1a5469d"}])
    # tree: 65208a85edf4a0d2c2f757ab655fb3ba2cd63bad
    r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[], author={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"}, committer={"name": "Jane Doe", "email": "jane@doe.com", "date": "2000-01-01T00:00:00Z"})
    # commit: f739e7ae2fd0e7b2bce99c073bcc7b57d713877e
    r.create_git_tag(tag="heavy-tag", message="This is a tag", object="f739e7ae2fd0e7b2bce99c073bcc7b57d713877e", type="commit", tagger={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"})
    # tag: b55a47efb4f8c891b6719a3d85a80c7f875e33ec
