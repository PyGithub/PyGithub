dict(
                ( key, {% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self._requester, element, completed = False ) )
                for key, element in attributes[ "{{ attribute.name }}" ].iteritems()
            )