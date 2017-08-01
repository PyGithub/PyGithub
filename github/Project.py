from github import GithubObject


class ProjectMixin(object):
    _preview_headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
    _obj_transformations = {
        'unicode': 'string',
        'str': 'string',
    }

    def _get_type(self, obj):
        '''
        Get type of the Github entity.

        :param obj:
        :return:
        '''

        t_obj = str(type(obj)).split("'>")[0].split("'")[-1]
        t_obj = self._obj_transformations.get(t_obj, t_obj)
        if t_obj == 'string' and len(obj) > 24 and '-' in obj and ':' in obj:
            t_obj = 'datetime'
        return t_obj.title()


class Project(ProjectMixin, GithubObject.CompletableGithubObject):
    '''
    Class represents Project.
    '''

    def _init_attributes(self):
        for attr in ['body', 'name', 'creator', 'url', 'created_at', 'html_url',
                     'number', 'updated_at', 'state', 'owner_url', 'columns_url', 'id']:
            self.__dict__['_{}'.format(attr)] = GithubObject.NotSet

    def _use_attributes(self, attributes):
        for attr_k, attr_v in attributes.items():
            mtd = "_make{0}Attribute".format(self._get_type(attr_v))
            self.__dict__['_{}'.format(attr_k)] = getattr(self, mtd)(attributes[attr_k])

    def __getattr__(self, item):
        _item = '_{}'.format(item)
        if self.__dict__.get(_item) is not None:
            self._completeIfNotSet(item)
        item = self.__dict__.get(_item)
        return item and item.value or item

    def get_columns(self):
        '''
        Returns columns of the project.
        :return:
        '''
        headers, data = self._requester.requestJsonAndCheck("GET", '/projects/{0}/columns'.format(self.id),
                                                            headers=self.__preview_headers)
        print data
