# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# ######################################################################
# #### This file is generated. Manual changes will likely be lost. #####
# ######################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking._base_github_object as bgo
import PyGithub.Blocking._send as snd
import PyGithub.Blocking._receive as rcv


class GitTag(bgo.SessionedGithubObject):
    """
    Base class: :class:`.SessionedGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :meth:`.Repository.get_git_tag`
    """

    def _initAttributes(self, message=rcv.Absent, object=rcv.Absent, sha=rcv.Absent, tag=rcv.Absent, tagger=rcv.Absent, url=rcv.Absent, **kwds):
        import PyGithub.Blocking.GitCommit
        super(GitTag, self)._initAttributes(**kwds)
        self.__message = rcv.Attribute("GitTag.message", rcv.StringConverter, message)
        self.__object = rcv.Attribute("GitTag.object", rcv.ClassConverter(self.Session, PyGithub.Blocking.GitCommit.GitCommit), object)
        self.__sha = rcv.Attribute("GitTag.sha", rcv.StringConverter, sha)
        self.__tag = rcv.Attribute("GitTag.tag", rcv.StringConverter, tag)
        self.__tagger = rcv.Attribute("GitTag.tagger", rcv.GitauthorConverter, tagger)
        self.__url = rcv.Attribute("GitTag.url", rcv.StringConverter, url)

    @property
    def message(self):
        """
        :type: :class:`string`
        """
        return self.__message.value

    @property
    def object(self):
        """
        :type: :class:`.GitCommit`
        """
        return self.__object.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        return self.__sha.value

    @property
    def tag(self):
        """
        :type: :class:`string`
        """
        return self.__tag.value

    @property
    def tagger(self):
        """
        :type: :class:`GitAuthor`
        """
        return self.__tagger.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        return self.__url.value
