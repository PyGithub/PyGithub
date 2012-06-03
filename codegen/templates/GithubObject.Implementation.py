{% if class.identity %}
    @property
    def _identity( self ):
        return {% include "GithubObject.Concatenation.py" with concatenation=class.identity only  %}
{% endif %}

    def _initAttributes( self ):
{% for attribute in class.attributes|dictsort:"name" %}
        self._{{ attribute.name }} = GithubObject.NotSet
{% endfor %}

    def _useAttributes( self, attributes ):
{% for attribute in class.attributes|dictsort:"name" %}

    {% with simple_or_complex=attribute.type.simple|yesno:"simple,complex_as_dict" %}
        if "{{ attribute.name }}" in attributes: # pragma no branch
        {% with template_name="GithubObject.IsInstance."|add:attribute.type.cardinality|add:"."|add:simple_or_complex|add:".py" %}
            assert attributes[ "{{ attribute.name }}" ] is None or {% include template_name with variable="attributes[ \""|add:attribute.name|add:"\" ]"|safe type=attribute.type only %}, attributes[ "{{ attribute.name }}" ]
        {% endwith %}
    {% endwith %}

    {% with simple_or_complex=attribute.type.simple|yesno:"simple,complex" %}
        {% with template_name="GithubObject.AttributeValue."|add:simple_or_complex|add:".py" %}
            self._{{ attribute.name }} = {% include template_name %}
        {% endwith %}
    {% endwith %}

{% endfor %}
