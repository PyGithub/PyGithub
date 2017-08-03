# -*- coding: utf-8 -*-
#
# Author: Bo Maryniuk <bo@suse.de>
#
# The MIT License (MIT)
# Copyright (C) 2017 SUSE Linux LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import github
from github import GithubObject, PaginatedList, Issue
import types


class EmptyObject(object):
    '''
    Dummy object, in case no structure returned.
    '''
    def __getattr__(self, item):
        return self.__dict__.get(item, self)

    def __str__(self):
        return ''


class OptKeyMap(dict):
    '''
    Optional values map. That is, acts like an array,
    but can provide alternative value to the key, if any.
    Otherwise returns the key as a value.
    '''
    def __init__(self, *elements, **kwargs):
        dict.__init__(self)
        for item in elements:
            self.append(item)
        self.update(kwargs)

    def __getitem__(self, item):
        return item in self and dict.__getitem__(self, item) or None

    def append(self, element):
        self[element] = None


class GithubObjectMixin(object):
    '''
    Create github objects on the fly
    '''
    _object_attributes = OptKeyMap()
    _preview_headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
    _obj_transformations = {
        'unicode': 'string',
        'str': 'string',
    }

    def _set_attribute(self, obj, o_type=None):
        '''
        Get type of the Github entity and set it.

        :param obj:
        :return:
        '''

        ref = None
        v_obj = obj or ''
        if o_type is None:
            t_obj = str(type(v_obj)).split("'>")[0].split("'")[-1]
            t_obj = self._obj_transformations.get(t_obj, t_obj)
        elif type(o_type) != str:
            ref = self._makeClassAttribute(o_type, obj)
        else:
            t_obj = o_type
        return ref or getattr(self, "_make{0}Attribute".format(t_obj.title()))(obj)

    def _init_attributes(self):
        '''
        Set empty attributes
        :return:
        '''
        for attr in self._object_attributes:
            self.__dict__['_{}'.format(attr)] = GithubObject.NotSet

    def __getattr__(self, item):
        _item = '_{}'.format(item)
        if self.__dict__.get(_item) is not None:
            self._completeIfNotSet(item)
        item = self.__dict__.get(_item)
        if item and hasattr(item, 'value'):
            item = item.value or item
        return item or EmptyObject()

    def _use_attributes(self, attributes):
        for attr_k, attr_v in attributes.items():
            self.__dict__['_{}'.format(attr_k)] = self._set_attribute(attr_v or '',
                                                                      o_type=self._object_attributes[attr_k])


class CardCreator(GithubObjectMixin, GithubObject.CompletableGithubObject):
    '''
    Class represents creator for Card
    '''
    _object_attributes = OptKeyMap('login', 'id', 'avatar_url', 'gravatar_id', 'url', 'html_url',
                                   'followers_url', 'following_url', 'gists_url', 'starred_url',
                                   'subscriptions_url', 'organizations_url', 'repos_url', 'events_url',
                                   'received_events_url', 'type', 'site_admin')


class Card(GithubObjectMixin, GithubObject.CompletableGithubObject):
    '''
    Class represents Card in the Column of the Project.
    '''
    _object_attributes = OptKeyMap('column_url', 'url', 'content_url', 'note', 'id',
                                   created_at='datetime', updated_at='datetime', creator=CardCreator)


class Column(GithubObjectMixin, GithubObject.CompletableGithubObject):
    '''
    Class represents column in the Project.
    '''
    _object_attributes = OptKeyMap('name', 'url', 'project_url', 'cards_url', 'id', 'creator',
                                   created_at='datetime', updated_at='datetime')

    def get_cards(self, column_id=None):
        '''
        Returns cards of the column.
        :return:
        '''
        return github.PaginatedList.PaginatedList(Card, self._requester,
                                                  "/projects/columns/{0}/cards".format(column_id or self.id),
                                                  None, headers=self._preview_headers)


class Project(GithubObjectMixin, GithubObject.CompletableGithubObject):
    '''
    Class represents Project.
    '''
    _object_attributes = OptKeyMap('body', 'name', 'creator', 'url', 'html_url',
                                   'number', 'state', 'owner_url', 'columns_url', 'id',
                                   created_at='datetime', updated_at='datetime')

    def get_columns(self, project_id=None):
        '''
        Returns columns of the project.
        :return:
        '''
        return github.PaginatedList.PaginatedList(Column, self._requester,
                                                  '/projects/{0}/columns'.format(project_id or self.id), None,
                                                  headers=self._preview_headers)
