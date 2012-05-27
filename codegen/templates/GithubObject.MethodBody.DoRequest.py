{% if method.request.postParameters %}
    {% if method.variadicParameter %}
        {% if method.variadicParameter.type.simple %}
        post_parameters = {{ method.variadicParameter.name }}s
        {% else %}
        post_parameters = [ {{ method.variadicParameter.name }}._identity for {{ method.variadicParameter.name }} in {{ method.variadicParameter.name }}s ]
        {% endif %}
    {% else %}
        post_parameters = {
        {% for parameter in method.mandatoryParameters %}
            "{{ parameter.name }}": {{ parameter.name }},
        {% endfor %}
        }
        {% for parameter in method.optionalParameters %}
        if {{ parameter.name }} is not DefaultValueForOptionalParameters:
            post_parameters[ "{{ parameter.name }}" ] = {{ parameter.name }}
        {% endfor %}
    {% endif %}
{% endif %}

        status, headers, data = self.__requester.request(
            "{{ method.request.verb }}",
            {% include "GithubObject.Concatenation.py" with concatenation=method.request.url only %},
{% if method.request.postParameters %}
            post_parameters
{% else %}
            None
{% endif %}
        )
