{% if method.request.postParameters %}
    {% if method.variadicParameter %}
        post_parameters = {{ method.variadicParameter.name }}s
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

{% if method.request.url_parameters %}
        url_parameters = {
    {% for parameter in method.request.url_parameters %}
            "{{ parameter.name }}": {% include "GithubObject.Concatenation.py" with concatenation=parameter.value only %},
    {% endfor %}
        }
{% endif %}

        status, headers, data = self.__requester.request(
            "{{ method.request.verb }}",
            {% include "GithubObject.Concatenation.py" with concatenation=method.request.url only %},
{% if method.request.url_parameters %}
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
