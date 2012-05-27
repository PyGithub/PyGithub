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

{% for attribute in class.attributes|dictsort:"name" %}
    @property
    def {{ attribute.name }}( self ):
{% if class.isCompletable %}
        self.__completeIfNeeded( self.__{{ attribute.name }} )
{% endif %}
        return self.__{{ attribute.name }}
{% endfor %}

{% for method in class.methods|dictsort:"name" %}
    def {{ method.name|join:"_" }}( {% include "GithubObject.Parameters.py" with function=method only %} ):
    {% if method.request %}
        {% include "GithubObject.MethodBody.DoRequest.py" %}
        {% include "GithubObject.MethodBody.UseResult.py" %}
    {% else %}
        pass
    {% endif %}
{% endfor %}

{% if class.identity %}
    @property
    def _identity( self ):
        return {% include "GithubObject.Concatenation.py" with concatenation=class.identity only  %}
{% endif %}

    def __initAttributes( self ):
{% for attribute in class.attributes|dictsort:"name" %}
        self.__{{ attribute.name }} = None
{% endfor %}

{% if class.isCompletable %}
    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True
{% endif %}

    def __useAttributes( self, attributes ):
{% for attribute in class.attributes|dictsort:"name" %}
        if "{{ attribute.name }}" in attributes and attributes[ "{{ attribute.name }}" ] is not None: # pragma no branch

{% if attribute.type.cardinality == "scalar" %}

    {% if attribute.type.simple %}
        {% if attribute.type.name == "string" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], ( str, unicode ) ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "integer" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], int ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "bool" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], bool ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
    {% else %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], dict ), attributes[ "{{ attribute.name }}" ]
    {% endif %}

{% else %}

    {% if attribute.type.simple %}
        {% if attribute.type.name == "string" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], list ) and ( len( attributes[ "{{ attribute.name }}" ] ) == 0 or isinstance( attributes[ "{{ attribute.name }}" ][ 0 ], ( str, unicode ) ) ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "integer" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], list ) and ( len( attributes[ "{{ attribute.name }}" ] ) == 0 or isinstance( attributes[ "{{ attribute.name }}" ][ 0 ], int ) ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "bool" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], list ) and ( len( attributes[ "{{ attribute.name }}" ] ) == 0 or isinstance( attributes[ "{{ attribute.name }}" ][ 0 ], bool ) ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
    {% else %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], list ) and ( len( attributes[ "{{ attribute.name }}" ] ) == 0 or isinstance( attributes[ "{{ attribute.name }}" ][ 0 ], dict ) ), attributes[ "{{ attribute.name }}" ]
    {% endif %}

{% endif %}

{% if attribute.type.cardinality == "scalar" %}

    {% if attribute.type.simple %}
            self.__{{ attribute.name }} = attributes[ "{{ attribute.name }}" ]
    {% else %}
            self.__{{ attribute.name }} = {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self.__requester, attributes[ "{{ attribute.name }}" ], completion = LazyCompletion )
    {% endif %}

{% else %}

    {% if attribute.type.simple %}
            self.__{{ attribute.name }} = attributes[ "{{ attribute.name }}" ]
    {% else %}
            self.__{{ attribute.name }} = [
                {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "{{ attribute.name }}" ]
            ]
    {% endif %}

{% endif %}

{% endfor %}
