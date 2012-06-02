{% if class.needsUrllib %}
import urllib
{% endif %}
{% if class.needsDatetime %}
import datetime
{% endif %}
{% if class.needsUrllib or class.needsDatetime %}
##########
{% endif %}

import GithubObject
{% if class.needsPaginatedList %}
import PaginatedList
{% endif %}

{% if class.dependencies %}
##########
    {% for dependency in class.dependencies %}
import {{ dependency }}
    {% endfor %}
{% endif %}

{% if class.isCompletable %}
class {{ class.name }}( GithubObject.GithubObject ):
{% else %}
class {{ class.name }}( GithubObject.BasicGithubObject ):
{% endif %}

{% include "GithubObject.PublicAttributes.py" %}

{% include "GithubObject.PublicMethods.py" %}

{% include "GithubObject.Implementation.py" %}
