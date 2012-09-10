# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net
##########
# This file is part of PyGithub. http://vincent-jacques.net/PyGithub
##########
# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
##########
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
##########
# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.
##########

{% if class.needsUrllib %}
import urllib
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
