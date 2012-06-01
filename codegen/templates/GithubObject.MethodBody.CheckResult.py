{% if method.type.name != "bool" %}
        self._checkStatus( status, data )
{% endif %}
