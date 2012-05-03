{% for dependency in class.dependencies %}
import {{ dependency }}
{% endfor %}

class {{ class.name }}( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )

{% for attribute in class.attributes %}
    @property
    def {{ attribute.name }}( self ):
        self.__completeIfNeeded( self.__{{ attribute.name }} )
        return self.__{{ attribute.name }}
{% endfor %}

    def __initAttributes( self ):
{% for attribute in class.attributes %}
        self.__{{ attribute.name }} = None
{% endfor %}

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()
        self.__completed = True

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.url,
            None,
            None
        )
        self.__useAttributes( result )

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
