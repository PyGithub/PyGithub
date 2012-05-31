{% for attribute in class.attributes|dictsort:"name" %}
    @property
    def {{ attribute.name }}( self ):
{% if class.isCompletable %}
        self._completeIfNotSet( self._{{ attribute.name }} )
{% endif %}
        return self._NoneIfNotSet( self._{{ attribute.name }} )
{% endfor %}
