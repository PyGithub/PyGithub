{% for attribute in class.attributes|dictsort:"name" %}
    @property
    def {{ attribute.name }}( self ):
{% if class.isCompletable %}
        self.__completeIfNeeded( self.__{{ attribute.name }} )
{% endif %}
        return self.__{{ attribute.name }}
{% endfor %}
