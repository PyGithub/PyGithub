{% for dependency in class.dependencies %}
import {{ dependency }}
{% endfor %}

class {{ class.name }}( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

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

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( result )
        self.__completed = True

{% for method in class.methods|dictsort:"name" %}
    def {{ method.name|join:"_" }}( {% include "GithubObject.Parameters.py" with function=method only %} ):
{% if method.request %}

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

        result = self.__github._dataRequest(
            "{{ method.request.verb }}",
            {% include "GithubObject.Concatenation.py" with concatenation=method.request.url only %},
            None,
{% if method.request.post_parameters %}
            post_parameters
{% else %}
            None
{% endif %}
        )

{% if method.type.name == "void" %}
        self.__useAttributes( result )
{% else %}

{% if method.type.cardinality == "scalar" %}
        return {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__github, result, lazy = True )
{% endif %}

{% if method.type.cardinality == "list" %}
        return [
            {% if method.type.name != class.name %}{{ method.type.name }}.{% endif %}{{ method.type.name }}( self.__github, element, lazy = True )
            for element in result
        ]
{% endif %}

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
