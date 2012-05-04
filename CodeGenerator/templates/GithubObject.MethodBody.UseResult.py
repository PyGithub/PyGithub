{% if method.is_mutation %}
        self.__useAttributes( result )
{% endif %}

{% if method.type.simple %}

{% if method.type.name == "bool" %}
        return result == 204
{% endif %}

{% else %}

{% if method.type.cardinality == "scalar" %}
        return {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__github, result, lazy = True )
{% endif %}

{% if method.type.cardinality == "list" %}
        return [
            {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__github, element, lazy = True )
            for element in result
        ]
{% endif %}

{% endif %}
