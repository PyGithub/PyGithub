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
            self.__complete()
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
    # @todo Remove '_identity' from the normalized json description
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
            self.__complete()

    def __complete( self ):
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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ {% for attribute in class.attributes|dictsort:"name" %}"{{ attribute.name }}", {% endfor %}], attribute

        # @todo No need to check if attribute is in attributes when attribute is mandatory
{% for attribute in class.attributes|dictsort:"name" %}
        if "{{ attribute.name }}" in attributes and attributes[ "{{ attribute.name }}" ] is not None:

{% if attribute.type.cardinality == "scalar" %}
{% if attribute.type.simple %}
    {% if attribute.type.name == "string" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], ( str, unicode ) )
    {% endif %}
    {% if attribute.type.name == "integer" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], int )
    {% endif %}
    {% if attribute.type.name == "bool" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], bool )
    {% endif %}
{% else %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], dict )
{% endif %}
{% endif %}

{% if attribute.type.cardinality == "list" %}
            assert isinstance( attributes[ "{{ attribute.name }}" ], list ) and ( len( attributes[ "{{ attribute.name }}" ] ) == 0 or isinstance( attributes[ "{{ attribute.name }}" ][ 0 ], dict ) )
{% endif %}

{% if attribute.type.cardinality == "scalar" %}
{% if attribute.type.simple %}
            self.__{{ attribute.name }} = attributes[ "{{ attribute.name }}" ]
{% else %}
            self.__{{ attribute.name }} = {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self.__requester, attributes[ "{{ attribute.name }}" ], completion = LazyCompletion )
{% endif %}
{% endif %}

{% if attribute.type.cardinality == "list" %}
            self.__{{ attribute.name }} = [
                {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self.__requester, element, completion = LazyCompletion )
                for element in attributes[ "{{ attribute.name }}" ]
            ]
{% endif %}

{% endfor %}
