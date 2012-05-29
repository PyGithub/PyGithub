{% if class.needsUrllib %}
import urllib
{% endif %}

import PaginatedList
from GithubObject import *

{% for dependency in class.dependencies %}
import {{ dependency }}
{% endfor %}

class {{ class.name }}( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
{% if class.isCompletable %}
        self.__completed = completion != LazyCompletion
        if completion == ImmediateCompletion:
            self.__complete() # pragma: no cover
{% endif %}

{% include "GithubObject.PublicAttributes.py" %}

{% include "GithubObject.PublicMethods.py" %}

{% include "GithubObject.Implementation.py" %}
