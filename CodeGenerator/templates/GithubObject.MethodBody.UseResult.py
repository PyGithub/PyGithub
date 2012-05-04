{% if method.is_mutation %}
        self.__useAttributes( data )
{% endif %}

{% if method.type.simple %}

{% if method.type.name == "bool" %}
        return status == 204
{% endif %}

{% else %}

{% if method.type.cardinality == "scalar" %}
        return {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__requester, data, lazy = True )
{% endif %}

{% if method.type.cardinality == "list" %}
        return [
            {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__requester, element, lazy = True )
            for element in data
        ]
{% endif %}

{% endif %}
