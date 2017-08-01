from github import GithubObject


class Project(GithubObject.CompletableGithubObject):
    __preview_headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
    __OBJ_TRANSFORMATIONS = {
        'unicode': 'string',
        'str': 'string',
    }

    def __get_type(self, obj):
        t_obj = str(type(obj)).split("'>")[0].split("'")[-1]
        return self.__OBJ_TRANSFORMATIONS.get(t_obj, t_obj).title()

    def _initAttributes(self):
        for attr in ['body', 'name', 'creator', 'url', 'created_at', 'html_url',
                     'number', 'updated_at', 'state', 'owner_url', 'columns_url', 'id']:
            self.__dict__['_{}'.format(attr)] = GithubObject.NotSet

    def _useAttributes(self, attributes):
        for attr_k, attr_v in attributes.items():
            mtd = "_make{0}Attribute".format(self.__get_type(attr_v))
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
