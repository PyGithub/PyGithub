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
            {% if parameter.type.name == "dict" %}
        assert isinstance( {{ parameter.name }}, dict ), {{ parameter.name }}
            {% endif %}
        {% else %}
        assert isinstance( {{ parameter.name }}, {{ parameter.type.name }}.{{ parameter.type.name }} ), {{ parameter.name }}
        {% endif %}

    {% else %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
        assert all( isinstance( element, ( str, unicode ) ) for element in {{ parameter.name }} ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
        assert all( isinstance( element, int ) for element in {{ parameter.name }} ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
        assert all( isinstance( element, bool ) for element in {{ parameter.name }} ), {{ parameter.name }}
            {% endif %}
        {% else %}
        assert all( isinstance( element, {{ parameter.type.name }}.{{ parameter.type.name }} ) for element in {{ parameter.name }} ), {{ parameter.name }}
        {% endif %}

    {% endif %}
{% endfor %}
{% for parameter in method.optionalParameters %}
    {% if parameter.type.cardinality == "scalar" %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
        assert {{ parameter.name }} is GithubObject.NotSet or isinstance( {{ parameter.name }}, ( str, unicode ) ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
        assert {{ parameter.name }} is GithubObject.NotSet or isinstance( {{ parameter.name }}, int ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
        assert {{ parameter.name }} is GithubObject.NotSet or isinstance( {{ parameter.name }}, bool ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "dict" %}
        assert {{ parameter.name }} is GithubObject.NotSet or isinstance( {{ parameter.name }}, dict ), {{ parameter.name }}
            {% endif %}
        {% else %}
        assert {{ parameter.name }} is GithubObject.NotSet or isinstance( {{ parameter.name }}, {{ parameter.type.name }}.{{ parameter.type.name }} ), {{ parameter.name }}
        {% endif %}

    {% else %}

        {% if parameter.type.simple %}
            {% if parameter.type.name == "string" %}
        assert {{ parameter.name }} is GithubObject.NotSet or all( isinstance( element, ( str, unicode ) ) for element in {{ parameter.name }} ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "integer" %}
        assert {{ parameter.name }} is GithubObject.NotSet or all( isinstance( element, int ) for element in {{ parameter.name }} ), {{ parameter.name }}
            {% endif %}
            {% if parameter.type.name == "bool" %}
        assert {{ parameter.name }} is GithubObject.NotSet or all( isinstance( element, bool ) for element in {{ parameter.name }} ), {{ parameter.name }}
            {% endif %}
        {% else %}
        assert {{ parameter.name }} is GithubObject.NotSet or all( isinstance( element, {{ parameter.type.name }}.{{ parameter.type.name }} ) for element in {{ parameter.name }} ), {{ parameter.name }}
        {% endif %}

    {% endif %}
{% endfor %}

{% if method.variadicParameter %}
    {% if method.variadicParameter.type.name != "@todo" %}
            {% if method.variadicParameter.type.simple %}
                {% if method.variadicParameter.type.name == "string" %}
        assert all( isinstance( {{ method.variadicParameter.name }}, ( str, unicode ) ) for {{ method.variadicParameter.name }} in {{ method.variadicParameter.name }}s ), {{ method.variadicParameter.name }}s
                {% endif %}
                {% if parameter.type.name == "integer" %}
        assert all( isinstance( {{ method.variadicParameter.name }}, int ) for {{ method.variadicParameter.name }} in {{ method.variadicParameter.name }}s ), {{ method.variadicParameter.name }}s
                {% endif %}
                {% if parameter.type.name == "bool" %}
        assert all( isinstance( {{ method.variadicParameter.name }}, bool ) for {{ method.variadicParameter.name }} in {{ method.variadicParameter.name }}s ), {{ method.variadicParameter.name }}s
                {% endif %}
            {% else %}
        assert all( isinstance( {{ method.variadicParameter.name }}, {{ method.variadicParameter.type.name }}.{{ method.variadicParameter.type.name }} ) for {{ method.variadicParameter.name }} in {{ method.variadicParameter.name }}s ), {{ method.variadicParameter.name }}s
            {% endif %}
    {% endif %}
{% endif %}
