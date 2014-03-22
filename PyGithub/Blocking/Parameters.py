# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>


class _Reset:
    pass
Reset = _Reset()


def dictionary(**args):
    d = dict()
    for k, v in args.iteritems():
        if v is Reset:
            d[k] = None
        elif v is not None:
            d[k] = v
    return d


def normalizeUser(user):
    import PyGithub.Blocking.User
    if isinstance(user, PyGithub.Blocking.User.User):
        return user.login
    elif isinstance(user, basestring):
        return user
    else:
        raise TypeError()


def normalizeRepository(repo):
    import PyGithub.Blocking.Repository
    if isinstance(repo, PyGithub.Blocking.Repository.Repository):
        return (repo.owner.login, repo.name)
    elif isinstance(repo, basestring):
        return repo.split("/")
    elif isinstance(repo, tuple):
        return repo
    else:
        raise TypeError()


def normalizeUserId(user):
    import PyGithub.Blocking.User
    if isinstance(user, PyGithub.Blocking.User.User):
        return user.id
    elif isinstance(user, int):
        return user
    else:
        raise TypeError()


def normalizeRepositoryId(repo):
    import PyGithub.Blocking.Repository
    if isinstance(repo, PyGithub.Blocking.Repository.Repository):
        return repo.id
    elif isinstance(repo, int):
        return repo
    else:
        raise TypeError()


def normalizeTeam(team):
    import PyGithub.Blocking.Team
    if isinstance(team, PyGithub.Blocking.Team.Team):
        return team.id
    elif isinstance(team, int):
        return team
    else:
        raise TypeError()


def normalizeString(s):
    if isinstance(s, basestring):
        return s
    else:
        raise TypeError()


def normalizeBool(b):
    if isinstance(b, bool):
        return b
    else:
        raise TypeError()


def normalizeInt(b):
    if isinstance(b, int):
        return b
    else:
        raise TypeError()


def normalizeStringReset(s):
    if isinstance(s, basestring):
        return s
    elif s is Reset:
        return s
    else:
        raise TypeError()


def normalizeBoolReset(b):
    if isinstance(b, bool):
        return b
    elif b is Reset:
        return b
    else:
        raise TypeError()


def normalizeTwoStringsString(s):
    if isinstance(s, basestring):
        return s.split("/")
    elif isinstance(s, tuple):
        return s
    else:
        raise TypeError()


def normalizeEnum(s, *values):
    if s in values:
        return s
    else:
        raise TypeError()


def normalizeList(normalizeElement, l):
    assert normalizeElement is normalizeRepository
    return ["/".join(normalizeElement(e)) for e in l]


def normalizeGitIgnoreTemplateString(tmpl):
    import PyGithub.Blocking.Github
    if isinstance(tmpl, PyGithub.Blocking.Github.Github.GitIgnoreTemplate):
        return tmpl.name
    elif isinstance(tmpl, basestring):
        return tmpl
    else:
        raise TypeError()


def normalizeGitAuthor(a):
    if isinstance(a, dict):
        return a
    else:
        raise TypeError()
