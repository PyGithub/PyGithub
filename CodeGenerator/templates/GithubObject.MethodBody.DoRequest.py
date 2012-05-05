{% if method.request.post_parameters %}
    {% if method.variadic_parameter %}
        post_parameters = {{ method.variadic_parameter.name }}s
    {% else %}
        post_parameters = {
        {% for parameter in method.mandatory_parameters %}
            "{{ parameter.name }}": {{ parameter.name }},
        {% endfor %}
        }
        {% for parameter in method.optional_parameters %}
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
{% if method.request.post_parameters %}
            post_parameters
{% else %}
            None
{% endif %}
        )
