{% if method.type.name != "bool" %}
        self._checkStatus( status, data )
{% endif %}

{% if method.isMutation %}
        self._useAttributes( data )
{% endif %}

{% if method.type.simple %}

    {% if method.type.cardinality == "scalar" %}

        {% if method.type.name == "bool" %}
        return status == 204
        {% endif %}

        {% if method.type.name == "@todo" %}
        return data
        {% endif %}

    {% endif %}

    {% if method.type.cardinality == "list" or method.type.cardinality == "dict" %}
        return data
    {% endif %}

{% else %}

    {% if method.type.cardinality == "scalar" %}
        return {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self._requester, data, completed = True )
    {% endif %}

    {% if method.type.cardinality == "list" %}
        return PaginatedList.PaginatedList( 
            {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }},
            self._requester,
            headers,
            data
        )
    {% endif %}

{% endif %}
