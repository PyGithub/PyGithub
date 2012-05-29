{% if method.request.postParameters %}
    {% if method.variadicParameter %}
        {% if method.variadicParameter.type.simple %}
        post_parameters = {{ method.variadicParameter.name }}s
        {% else %}
        post_parameters = [ {{ method.variadicParameter.name }}._identity for {{ method.variadicParameter.name }} in {{ method.variadicParameter.name }}s ]
        {% endif %}
    {% else %}
        {% if method.mandatoryParameters %}
        post_parameters = {
            {% for parameter in method.mandatoryParameters %}
            "{{ parameter.name }}": {{ parameter.name }},
            {% endfor %}
        }
        {% else %}
        post_parameters = dict()
        {% endif %}
        {% for parameter in method.optionalParameters %}
        if {{ parameter.name }} is not DefaultValueForOptionalParameters:
            post_parameters[ "{{ parameter.name }}" ] = {{ parameter.name }}
        {% endfor %}
    {% endif %}
{% else %}
    {% if method.optionalParameters %}
        url_parameters = dict()
        {% for parameter in method.optionalParameters %}
        if {{ parameter.name }} is not DefaultValueForOptionalParameters:
            url_parameters[ "{{ parameter.name }}" ] = {{ parameter.name }}
        {% endfor %}
    {% endif %}
{% endif %}

{% if method.request.urlParameters %}
        url_parameters = {
    {% for parameter in method.request.urlParameters %}
            "{{ parameter.name }}": {% include "GithubObject.Concatenation.py" with concatenation=parameter.value only %},
    {% endfor %}
        }
{% endif %}

        status, headers, data = self.__requester.request(
            "{{ method.request.verb }}",
            {% include "GithubObject.Concatenation.py" with concatenation=method.request.url only %},
{% if method.request.urlParameters or not method.request.postParameters and method.optionalParameters %}
            url_parameters,
{% else %}
            None,
{% endif %}
{% if method.request.postParameters %}
            post_parameters
{% else %}
            None
{% endif %}
        )
