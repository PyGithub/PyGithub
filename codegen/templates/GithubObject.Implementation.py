{% if class.identity %}
    @property
    def _identity( self ):
        return {% include "GithubObject.Concatenation.py" with concatenation=class.identity only  %}
{% endif %}

    def _initAttributes( self ):
{% for attribute in class.attributes|dictsort:"name" %}
        self._{{ attribute.name }} = GithubObject.NotSet
{% endfor %}

    def _useAttributes( self, attributes ):
{% for attribute in class.attributes|dictsort:"name" %}
        if "{{ attribute.name }}" in attributes: # pragma no branch

{% if attribute.type.cardinality == "scalar" %}

    {% if attribute.type.simple %}
        {% if attribute.type.name == "string" %}
            assert attributes[ "{{ attribute.name }}" ] is None or isinstance( attributes[ "{{ attribute.name }}" ], ( str, unicode ) ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "integer" %}
            assert attributes[ "{{ attribute.name }}" ] is None or isinstance( attributes[ "{{ attribute.name }}" ], int ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
        {% if attribute.type.name == "bool" %}
            assert attributes[ "{{ attribute.name }}" ] is None or isinstance( attributes[ "{{ attribute.name }}" ], bool ), attributes[ "{{ attribute.name }}" ]
        {% endif %}
    {% else %}
            assert attributes[ "{{ attribute.name }}" ] is None or isinstance( attributes[ "{{ attribute.name }}" ], dict ), attributes[ "{{ attribute.name }}" ]
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
            self._{{ attribute.name }} = attributes[ "{{ attribute.name }}" ]
    {% else %}
            self._{{ attribute.name }} = None if attributes[ "{{ attribute.name }}" ] is None else {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self._requester, attributes[ "{{ attribute.name }}" ], completed = False )
    {% endif %}

{% else %}

    {% if attribute.type.simple %}
            self._{{ attribute.name }} = attributes[ "{{ attribute.name }}" ]
    {% else %}
            self._{{ attribute.name }} = [
                {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self._requester, element, completed = False )
                for element in attributes[ "{{ attribute.name }}" ]
            ]
    {% endif %}

{% endif %}

{% endfor %}
