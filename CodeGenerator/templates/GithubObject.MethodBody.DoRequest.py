{% if method.request.post_parameters %}
        post_parameters = {
    {% for parameter in method.mandatory_parameters %}
            "{{ parameter.name }}": {{ parameter.name }},
    {% endfor %}
        }
    {% for parameter in method.optional_parameters %}
        if {{ parameter.name }} is not None:
            post_parameters[ "{{ parameter.name }}" ] = {{ parameter.name }}
    {% endfor %}
{% endif %}

        status, headers, data = self.__requester.request(
            "{{ method.request.verb }}",
            {% include "GithubObject.Concatenation.py" with concatenation=method.request.url only %},
            None,
{% if method.request.post_parameters %}
            post_parameters
{% else %}
            None
{% endif %}
        )
