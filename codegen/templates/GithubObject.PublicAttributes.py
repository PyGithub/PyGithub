{% for attribute in class.attributes|dictsort:"name" %}
    @property
    def {{ attribute.name }}( self ):
{% if class.isCompletable %}
        self._completeIfNeeded( self._{{ attribute.name }} )
{% endif %}
        return self._{{ attribute.name }}
{% endfor %}
