Webhook
=======

Creating and Listening to Webhooks with PyGithub and Pyramid
------------------------------------------------------------

To receive a continuous stream of events from GitHub, you can set up a WSGI app using Pyramid to handle incoming POST requests. This allows you to automate responses to GitHub events, such as push or pull request updates.

Overview
--------

The example below demonstrates how to create a webhook listener using Pyramid and PyGithub. This webhook will listen for `pull_request` and `push` events, triggering specific actions when a PR is opened, closed, merged, or synced, or when a commit is pushed.

For reference, this example is adapted from `GitHub's platform samples <https://github.com/github/platform-samples/blob/master/api/python/building-a-ci-server/server.py>`__. A comprehensive list of event types that GitHub webhooks support is available in the `GitHub Webhooks documentation <https://developer.github.com/v3/issues/events/>`__.

Setting Up the Webhook Listener
-------------------------------

.. code-block:: python

    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    from pyramid.view import view_config, view_defaults
    from pyramid.response import Response
    from github import Github

    ENDPOINT = "webhook"

    @view_defaults(
        route_name=ENDPOINT, renderer="json", request_method="POST"
    )
    class PayloadView:
        """
        Handles incoming GitHub webhook payloads.
        The view is triggered only for JSON payloads sent via POST requests.
        """
        def __init__(self, request):
            self.request = request
            self.payload = self.request.json

        @view_config(header="X-Github-Event:push")
        def payload_push(self):
            """Handles push events."""
            print("Number of commits in push:", len(self.payload['commits']))
            return Response("success")

        @view_config(header="X-Github-Event:pull_request")
        def payload_pull_request(self):
            """Handles pull request events."""
            print("Pull Request action:", self.payload['action'])
            print("Number of commits in PR:", self.payload['pull_request']['commits'])
            return Response("success")

        @view_config(header="X-Github-Event:ping")
        def payload_else(self):
            """Handles GitHub's ping event when a webhook is created."""
            print("Webhook created with ID {}!".format(self.payload["hook"]["id"]))
            return {"status": 200}

Creating a Webhook Programmatically
-----------------------------------

Instead of manually configuring a webhook via GitHub's UI, you can create it programmatically using PyGithub:

.. code-block:: python

    def create_webhook():
        """
        Creates a webhook for a specified GitHub repository.
        """
        USERNAME = ""
        PASSWORD = ""
        OWNER = ""
        REPO_NAME = ""
        EVENTS = ["push", "pull_request"]
        HOST = ""

        config = {
            "url": "http://{host}/{endpoint}".format(host=HOST, endpoint=ENDPOINT),
            "content_type": "json"
        }

        g = Github(USERNAME, PASSWORD)
        repo = g.get_repo("{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
        repo.create_hook("web", config, EVENTS, active=True)

Running the Webhook Server
--------------------------

.. code-block:: python

    if __name__ == "__main__":
        config = Configurator()
        create_webhook()
        config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
        config.scan()
        app = config.make_wsgi_app()
        server = make_server("0.0.0.0", 80, app)
        server.serve_forever()

Testing the Webhook
-------------------

To test the webhook, you can use API debugging tools such as:

- **Beeceptor** (`https://beeceptor.com/ <https://beeceptor.com/>`__): Allows you to inspect webhook requests and simulate responses.
- **PostBin** (`https://www.postb.in/ <https://www.postb.in/>`__): Provides an endpoint to capture incoming webhook data for debugging.


Outputs from a server configured as above:

.. code-block:: console

    x.y.w.z - - [15/Oct/2018 23:49:19] "POST /webhook HTTP/1.1" 200 15
    Pinged! Webhook created with id <redacted id>!
    No. commits in push: 1
    x.y.w.z - - [15/Oct/2018 23:49:32] "POST /webhook HTTP/1.1" 200 7
    PR synchronize
    x.y.w.z - - [15/Oct/2018 23:49:33] "POST /webhook HTTP/1.1" 200 7
    No. Commits in PR: 10
    PR closed
    x.y.w.z - - [15/Oct/2018 23:49:56] "POST /webhook HTTP/1.1" 200 7
    No. Commits in PR: 10
    x.y.w.z - - [15/Oct/2018 23:50:00] "POST /webhook HTTP/1.1" 200 7
    PR reopened
    No. Commits in PR: 10
