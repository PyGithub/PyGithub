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

# There is no API to create users, so we need to create them manually
zeus = b.Login("zeus", "password1-zeus").Build().get_authenticated_user()
verify(zeus, site_admin=True, suspended_at=None)
ensure(zeus, name="Zeus, god of the sky", email="ghe-zeus@jacquev6.net", location="Olympus", blog="http://jacquev6.net/zeus", hireable=False, company="Zeus Software")

poseidon = b.Login("poseidon", "password1-poseidon").Build().get_authenticated_user()
verify(poseidon, site_admin=True, suspended_at=None)
ensure(poseidon, name="Poseidon, god of the sea", email="ghe-poseidon@jacquev6.net", location="Deep in the sea", blog="http://jacquev6.net/poseidon", hireable=False, company="Poseidon Software")

assert b.Build().get_user("morpheus").suspended_at

antigone = b.Login("antigone", "password1-antigone").Build().get_authenticated_user()
verify(antigone, site_admin=False, suspended_at=None)
ensure(antigone, name="Antigone", email="ghe-antigone@jacquev6.net", location="Greece", blog="http://jacquev6.net/antigone", hireable=False, company="Antigone Software")

electra = b.Login("electra", "password1-electra").Build().get_authenticated_user()
verify(electra, site_admin=False, suspended_at=None)
ensure(electra, name="Electra", email="ghe-electra@jacquev6.net", location="Greece", blog="http://jacquev6.net/electra", hireable=False, company="Electra Software")

penelope = b.Login("penelope", "password1-penelope").Build().get_authenticated_user()
verify(penelope, site_admin=False, suspended_at=None)
ensure(penelope, name=None, email=None, location=None, blog=None, hireable=False, company=None)
