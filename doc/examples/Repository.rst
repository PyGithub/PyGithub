Repository
==========

Get repository topics
---------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_topics()
    [u'pygithub', u'python', u'github', u'github-api']

Get count of stars
------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.stargrazers_count
    2086

Get list of open issues
--------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> open_issues = repo.get_issues(state='open')
    >>> for issue in open_issues:
    ...    print(issue)
    ...
	Issue(title="How to get public events?", number=913)
	Issue(title="Prevent .netrc from overwriting Auth header", number=910)
	Issue(title="Cache fetch responses", number=901)
	Issue(title="Is suspended_users for github enterprise implemented in NamedUser?", number=900)
	Issue(title="Adding migration api wrapper", number=899)

Get all the labels of the repository
------------------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> labels = repo.get_labels()
    >>> for label in labels:
    ...    print(label)
    ...
    Label(name="Hacktoberfest")
    Label(name="WIP")
    Label(name="bug")
    Label(name="documentation")

Subscribe to Repository Events
------------------------------------

To receive a continuous stream of events, one can set up a Flask app to listen for
events at a given repository.

The below code sets up a listener which creates and utilizes a webhook. Using
'pull_request' and 'push' for the EVENT attributes, any time a PR is opened, closed, or merged, or a commit is pushed,
Github sends a POST containing a payload with information about the PR/push and its state.

.. code-block:: python

    from flask import Flask, request, jsonify
    from github import Github
    import json

    app = Flask(__name__)

    USERNAME = ""
    PASSWORD = ""
    OWNER = ""
    REPO_NAME = ""
    EVENT = ""  # list can be found at https://developer.github.com/v3/issues/events/
    HOST = ""
    ENDPOINT = ""

    config = {
        "url": "{host}/{endpoint}".format(host=HOST, endpoint=ENDPOINT),
        "content_type": "x-www-form-urlencoded"
    }

    events = ["push", "pull_request"]

    g = Github(USERNAME, PASSWORD)
    repo = g.get_repo("{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
    repo.create_hook("my-webhook", config, events, active=True)

    @app.route("/{endpoint}".format(endpoint=ENDPOINT), methods=['POST'])
    def recieve_event():
        data = request.form
        payload = json.loads(data['payload'])
        return jsonify(success=True)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=80)


Assuming we get to the successful return statement, this
is some of the data we could expect to see in the payload for a Pull Request:

.. code-block:: python

    >>> payload['action']
    'closed'
    >>> payload['number']
    1
    >>> payload['pull_request']['id']
    222619227
    >>> payload['pull_request']['commits']
    2