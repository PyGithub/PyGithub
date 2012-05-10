{% if method.isMutation %}
        self.__useAttributes( data )
{% endif %}

{% if method.type.simple %}

{% if method.type.cardinality == "scalar" %}

{% if method.type.name == "@todo" %}
        return data
{% endif %}

{% if method.type.name == "bool" %}
        return status == 204
{% endif %}

{% endif %}

{% if method.type.cardinality == "list" %}
        return data
{% endif %}

{% else %}

{% if method.type.cardinality == "scalar" %}
        return {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__requester, data, lazy = True )
{% endif %}

{% if method.type.cardinality == "list" %}
        return PaginatedList.PaginatedList( 
            {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }},
            self.__requester,
            headers,
            data
        )
{% endif %}

{% endif %}
