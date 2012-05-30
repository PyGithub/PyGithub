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
            assert all( isinstance( element, ( str, unicode ) ) for element in attributes[ "{{ attribute.name }}" ] ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "integer" %}
            assert all( isinstance( element, int ) for element in attributes[ "{{ attribute.name }}" ] ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "bool" %}
            assert all( isinstance( element, bool ) for element in attributes[ "{{ attribute.name }}" ] ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
    {% else %}
            assert all( isinstance( element, dict ) for element in attributes[ "{{ attribute.name }}" ] ), attributes[ "{{ attribute.name }}" ]
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
