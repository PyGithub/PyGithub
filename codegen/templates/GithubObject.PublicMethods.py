{% for method in class.methods|dictsort:"name" %}
    def {{ method.name|join:"_" }}( {% include "GithubObject.Parameters.py" with function=method only %} ):
        {% include "GithubObject.MethodBody.CheckArguments.py" %}
        {% include "GithubObject.MethodBody.DoRequest.py" %}
        {% include "GithubObject.MethodBody.CheckResult.py" %}
        {% include "GithubObject.MethodBody.UseResult.py" %}
{% endfor %}
