Webhook
==========

Creating and Listening to Webhooks with PyGithub and Pyramid
------------------------------------

To receive a continuous stream of events, one can set up a wsgiref app using Pyramid to handle
incoming POST requests.

The below code sets up a listener which creates and utilizes a webhook. Using
'pull_request' and 'push' for the EVENT attributes, any time a PR is opened, closed, merged, or synced, or a commit is pushed,
Github sends a POST containing a payload with information about the PR/push and its state.

The below example was drawn largely from `Github's Examples <https://github.com/github/platform-samples/blob/master/api/python/building-a-ci-server/server.py>`__
on working with Webhooks. A list of all applicable event types for Webhooks can be found in `Github's documentation <https://developer.github.com/v3/issues/events/>`__

.. code-block:: python

    from __future__ import print_function

    from wsgiref.simple_server import make_server
    from pyramid.config import Configurator
    from pyramid.view import view_config, view_defaults
    from pyramid.response import Response
    from github import Github

    ENDPOINT = "webhook"

    @view_defaults(
        route_name=ENDPOINT, renderer="json", request_method="POST"
    )
    class PayloadView(object):
        """
        View receiving of Github payload. By default, this view it's fired only if
        the request is json and method POST.
        """

        def __init__(self, request):
            self.request = request
            # Payload from Github, it's a dict
            self.payload = self.request.json

        @view_config(header="X-Github-Event:push")
        def payload_push(self):
            """This method is a continuation of PayloadView process, triggered if
            header HTTP-X-Github-Event type is Push"""
            print("No. commits in push:", len(self.payload['commits']))
            return Response("success")

        @view_config(header="X-Github-Event:pull_request")
        def payload_pull_request(self):
            """This method is a continuation of PayloadView process, triggered if
            header HTTP-X-Github-Event type is Pull Request"""
            print("PR", self.payload['action'])
            print("No. Commits in PR:", self.payload['pull_request']['commits'])

            return Response("success")

        @view_config(header="X-Github-Event:ping")
        def payload_else(self):
            print("Pinged! Webhook created with id {}!".format(self.payload["hook"]["id"]))
            return {"status": 200}


    def create_webhook():
        """ Creates a webhook for the specified repository.

        This is a programmatic approach to creating webhooks with PyGithub's API. If you wish, this can be done
        manually at your repository's page on Github in the "Settings" section. There is a option there to work with
        and configure Webhooks.
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


    if __name__ == "__main__":
        config = Configurator()

        create_webhook()

        config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
        config.scan()

        app = config.make_wsgi_app()
        server = make_server("0.0.0.0", 80, app)
        server.serve_forever()


Outputs from a server configured as above:

.. code-block:: python

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
