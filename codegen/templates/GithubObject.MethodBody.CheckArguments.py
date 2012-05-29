{% for parameter in method.mandatoryParameters %}
    {% if parameter.type.cardinality == "scalar" %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
        assert isinstance( {{ parameter.name }}, ( str, unicode ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
        assert isinstance( {{ parameter.name }}, int ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
        assert isinstance( {{ parameter.name }}, bool ), {{ parameter.name }}
            {% endif %}
        {% else %}
        assert isinstance( {{ parameter.name }}, {{ parameter.type.name }}.{{ parameter.type.name }} ), {{ parameter.name }}
        {% endif %}

    {% else %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
        assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], ( str, unicode ) ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
        assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], int ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
        assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], bool ) ), {{ parameter.name }}
            {% endif %}
        {% else %}
        assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], {{ parameter.type.name }}.{{ parameter.type.name }} ) ), {{ parameter.name }}
        {% endif %}

    {% endif %}
{% endfor %}
{% for parameter in method.optionalParameters %}
    {% if parameter.type.name != "@todo" %}
        if {{ parameter.name }} is not DefaultValueForOptionalParameters:
    {% endif %}

    {% if parameter.type.cardinality == "scalar" %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
            assert isinstance( {{ parameter.name }}, ( str, unicode ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
            assert isinstance( {{ parameter.name }}, int ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
            assert isinstance( {{ parameter.name }}, bool ), {{ parameter.name }}
            {% endif %}
        {% else %}
            assert isinstance( {{ parameter.name }}, {{ parameter.type.name }}.{{ parameter.type.name }} ), {{ parameter.name }}
        {% endif %}

    {% else %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
            assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], ( str, unicode ) ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
            assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], int ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
            assert isinstance( {{ parameter.name }}, list ) and ( len( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], bool ) ), {{ parameter.name }}
            {% endif %}
            {% else %}
            assert isinstance( {{ parameter.name }}, list ) and ( {{ parameter.name }} ) == 0 or isinstance( {{ parameter.name }}[ 0 ], {{ parameter.type.name }}.{{ parameter.type.name }} ) ), {{ parameter.name }}
        {% endif %}

    {% endif %}
{% endfor %}

{% if method.variadicParameter %}
    {% if method.variadicParameter.type.name != "@todo" %}
            {% if method.variadicParameter.type.simple %}
                {% if method.variadicParameter.type.name == "string" %}
        assert len( {{ method.variadicParameter.name }}s ) == 0 or isinstance( {{ method.variadicParameter.name }}s[ 0 ], ( str, unicode ) ), {{ method.variadicParameter.name }}s
                {% endif %}
                {% if parameter.type.name == "integer" %}
        assert len( {{ method.variadicParameter.name }}s ) == 0 or isinstance( {{ method.variadicParameter.name }}s[ 0 ], int ), {{ method.variadicParameter.name }}s
                {% endif %}
                {% if parameter.type.name == "bool" %}
        assert len( {{ method.variadicParameter.name }}s ) == 0 or isinstance( {{ method.variadicParameter.name }}s[ 0 ], bool ), {{ method.variadicParameter.name }}s
                {% endif %}
            {% else %}
        assert len( {{ method.variadicParameter.name }}s ) == 0 or isinstance( {{ method.variadicParameter.name }}s[ 0 ], {{ method.variadicParameter.type.name }}.{{ method.variadicParameter.type.name }} ), {{ method.variadicParameter.name }}s
            {% endif %}
    {% endif %}
{% endif %}
