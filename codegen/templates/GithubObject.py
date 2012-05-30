{% if class.needsUrllib %}
import urllib
##########
{% endif %}

import GithubObject
{% if class.needsPaginatedList %}
import PaginatedList
{% endif %}
{% if class.needsDefaultValue %}
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
{% endif %}

{% if class.dependencies %}
##########
    {% for dependency in class.dependencies %}
import {{ dependency }}
    {% endfor %}
{% endif %}

{% if class.isCompletable %}
class {{ class.name }}( GithubObject.CompletableGithubObject ):
{% else %}
class {{ class.name }}( GithubObject.GithubObject ):
{% endif %}

{% include "GithubObject.PublicAttributes.py" %}

{% include "GithubObject.PublicMethods.py" %}

{% include "GithubObject.Implementation.py" %}
