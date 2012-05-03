class {{ class.name }}( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

{% for attribute in class.attributes %}
    @property
    def {{ attribute.name }}( self ):
        if self.__{{ attribute.name }} is None:
            self.__completeIfNeeded()
        return self.__{{ attribute.name }}
{% endfor %}

    def __initAttributes( self ):
{% for attribute in class.attributes %}
        self.__{{ attribute.name }} = None
{% endfor %}

    def __completeIfNeeded( self ):
        if not self.__completed:
            self.__complete()
        self.__completed = True

    def __complete( self ):
        pass

{% for method in class.methods|dictsort:"name" %}
    def {{ method.name|join:"_" }}( {% include "GithubObject.Parameters.py" with function=method only %} ):
{% if method.request %}
        result = self.__github._dataRequest(
            "{{ method.request.verb }}",
            {% include "GithubObject.Concatenation.py" with concatenation=method.request.url only %},
            None,
            None
        )

{% if method.type.cardinality == "scalar" %}
        return {{ method.type.name }}.{{ method.type.name }}( self.__github, result, lazy = True )
{% endif %}

{% if method.type.cardinality == "list" %}
        return [
            {{ method.type.name }}.{{ method.type.name }}( self.__github, element, lazy = True )
            for element in result
        ]
{% endif %}

{% else %}
        pass
{% endif %}
{% endfor %}

    def __useAttributes( self, attributes ):
{% for attribute in class.attributes %}
        if "{{ attribute.name }}" in attributes:
            self.__{{ attribute.name }} = attributes[ "{{ attribute.name }}" ]
{% endfor %}
