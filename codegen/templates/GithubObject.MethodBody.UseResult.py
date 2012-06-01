{% if method.isMutation %}
        self._useAttributes( data )
{% else %}
    {% if method.type.name != "void" %}
        return {% include "GithubObject.MethodBody.ReturnValue.py" %}
    {% endif %}
{% endif %}
