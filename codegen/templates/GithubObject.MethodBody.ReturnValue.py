{% if method.type.name == "bool" %}status == 204
{% else %}{% if method.type.simple %}data
{% else %}{% if method.type.cardinality == "scalar" %}{% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self._requester, data, completed = True )
{% else %}PaginatedList.PaginatedList( 
            {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }},
            self._requester,
            headers,
            data
        )
{% endif %}
{% endif %}
{% endif %}
