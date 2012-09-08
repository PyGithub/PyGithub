You don't normaly create instances of any class but `Github`.
You obtain instances through calls to `search_`, `get_` and `create_` methods.

Methods returning an "iterator of `SomeType`" return an iterator which yields instances of `SomeType`.
This implements lazy [pagination requests](http://developer.github.com/v3/#pagination).
You can use this iterator in a `for f in user.get_followers():` loop or with any [itertools](http://docs.python.org/library/itertools.html) functions,
but you cannot know the number of objects returned before the end of the iteration.
If that's really what you need, you cant use `len( list( user.get_followers() ) )`, which does all the requests needed to enumerate the user's followers.
Note that there is often an attribute giving this value (in that case `user.followers`).

Class `Github`
==============

Constructed from user's login and password or OAuth token or nothing:

    g = Github( login, password )
    g = Github( token )
    g = Github()

You can add an argument `base_url = "http://my.enterprise.com:8080/path/to/github"` to connect to a local install of Github (ie. Github Enterprise).
Another argument, that can be passed is `timeout` which has default value `10`.

Attributes
----------
* `rate_limiting`: tuple of two integers: remaining and limit, as explained in [Rate Limiting](http://developer.github.com/v3/#rate-limiting)

Methods
-------
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`
* `get_gist( id )`: `Gist`
    * `id`: string
* `get_gists()`: iterator of `Gist`
* `search_repos( keyword )`: iterator of `Repository`
* `legacy_search_repos( keyword, [language] )`: iterator of `Repository`
    * `keyword`: string
    * `language`: string
* `legacy_search_users( keyword )`: iterator of `NamedUser`
    * `keyword`: string
* `legacy_search_user_by_email( email )`: `NamedUser`
    * `email`: string
* `render_markdown( text, [context] )`: string
    * `text`: string
    * `context`: `Repository`

Class `GithubException`
=======================

Attributes
----------
* `status`: integer
* `data`: dict

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
