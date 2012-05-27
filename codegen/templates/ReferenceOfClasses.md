You don't normaly create instances of any class but `Github`.
You obtain instances through calls to `get_` and `create_` methods.

Class `Github`
==============
* Constructed from user's login and password or OAuth token
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`
* `get_gist( id )`: `Gist`
* `get_gists()`: list of `Gist`
* `rate_limiting`: tuple of two integers: remaining and limit, as explained in [Rate Limiting](http://developer.github.com/v3/#rate-limiting)

{% for class in classes|dictsort:"name" %}
Class `{{ class.name }}`
======={% for char in class.name %}={% endfor %}=

Attributes
----------
{% for attribute in class.attributes|dictsort:"name" %}* `{{ attribute.name }}`{% include "ReferenceOfClasses.Type.md" with type=attribute.type only %}
{% endfor %}

{% regroup class.methods|dictsort:"group" by group as method_groups %}

{% for method_group in method_groups %}

{{ method_group.grouper|capfirst }}
{% for letter in method_group.grouper %}-{% endfor %}

{% for method in method_group.list %}

* `{{ method.name|join:"_" }}({% include "ReferenceOfClasses.Parameters.md" with function=method only %})`{% include "ReferenceOfClasses.Type.md" with type=method.type only %}

{% for parameter in method.mandatoryParameters %}
    * `{{ parameter.name }}`{% include "ReferenceOfClasses.Type.md" with type=parameter.type only %}
{% endfor %}
{% for parameter in method.optionalParameters %}
    * `{{ parameter.name }}`{% include "ReferenceOfClasses.Type.md" with type=parameter.type only %}
{% endfor %}
{% if method.variadicParameter %}
    * `{{ method.variadicParameter.name }}`{% include "ReferenceOfClasses.Type.md" with type=method.variadicParameter.type only %}
{% endif %}

{% endfor %}

{% endfor %}

{% endfor %}
