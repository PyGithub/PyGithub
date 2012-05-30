{% if class.needsUrllib %}
import urllib
{% endif %}

import PaginatedList
from GithubObject import *

{% for dependency in class.dependencies %}
import {{ dependency }}
{% endfor %}

class {{ class.name }}( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
{% if class.isCompletable %}
        self.__completed = completed
{% endif %}

{% include "GithubObject.PublicAttributes.py" %}

{% include "GithubObject.PublicMethods.py" %}

{% include "GithubObject.Implementation.py" %}
