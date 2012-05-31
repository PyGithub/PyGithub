{% for parameter in method.mandatoryParameters %}
    {% if parameter.type.name != "@todo" %}
        {% with simple_or_complex=parameter.type.simple|yesno:"simple,complex" %}
            {% with template_name="GithubObject.IsInstance."|add:parameter.type.cardinality|add:"."|add:simple_or_complex|add:".py" %}
        assert {% include template_name with variable=parameter.name type=parameter.type only %}, {{ parameter.name }}
            {% endwith %}
        {% endwith %}
    {% endif %}
{% endfor %}

{% for parameter in method.optionalParameters %}
    {% if parameter.type.name != "@todo" %}
        {% with simple_or_complex=parameter.type.simple|yesno:"simple,complex" %}
            {% with template_name="GithubObject.IsInstance."|add:parameter.type.cardinality|add:"."|add:simple_or_complex|add:".py" %}
        assert {{ parameter.name }} is GithubObject.NotSet or {% include template_name with variable=parameter.name type=parameter.type only %}, {{ parameter.name }}
            {% endwith %}
        {% endwith %}
    {% endif %}
{% endfor %}

{% if method.variadicParameter %}
    {% with simple_or_complex=method.variadicParameter.type.simple|yesno:"simple,complex" %}
        {% with template_name="GithubObject.IsInstance.list."|add:simple_or_complex|add:".py" %}
        assert {% include template_name with variable=method.variadicParameter.name|add:"s" type=method.variadicParameter.type only %}, {{ method.variadicParameter.name }}s
        {% endwith %}
    {% endwith %}
{% endif %}
