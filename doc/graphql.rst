Github GraphQL
==============

The PyGithub project primarily accesses the Github REST API v3. However, Github has started to provide
more functionality behind a separate GraphQL API. Further benefits of the GraphQL endpoint is that the
caller has full control over the structure and complexity (or simplicity) of the response, hence can reduce
both number of calls and size of transferred data.

PyGithub provides access to the GraphQL API while providing results using the usual object-oriented PyGithub objects
hierarchy.

This documents the current support for the GraphQL API.

GraphQL Classes
---------------

Some PyGithub classes represent GraphQL schemas, where no equivalent Github REST API schema exists.
GraphQL API data of those classes are translated (see ``as_rest_api_attributes(attributes)`` below)
into REST API equivalent data and backed by ordinary PyGithub classes.

A good example is ``RepositoryDiscussion``:

.. code-block:: python

    class RepositoryDiscussion(GraphQlObject, DiscussionBase):
        """
        This class represents GraphQL Discussion.

        The reference can be found here
        https://docs.github.com/en/graphql/reference/objects#discussion

        """

    ...

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        # super class is a REST API GithubObject, attributes are coming from GraphQL
        super()._useAttributes(as_rest_api_attributes(attributes))
        if "answer" in attributes:  # pragma no branch
            self._answer = self._makeClassAttribute(
                github.RepositoryDiscussionComment.RepositoryDiscussionComment, attributes["answer"]
            )
        if "bodyText" in attributes:  # pragma no branch
            self._body_text = self._makeStringAttribute(attributes["bodyText"])
    ...

Query
-----

GraphQL data can be retrieved by GraphQL queries. A good example can be found in :class:`github.Repository.Repository` method ``get_discussion``.

GraphQL queries can be sent to the Github GraphQL API via these methods:

- :func:`github.Requester.Requester.graphql_node`
- :func:`github.Requester.Requester.graphql_node_class`
- :func:`github.Requester.Requester.graphql_query`
- :func:`github.Requester.Requester.graphql_query_class`

Mutation
--------

The GraphQL API can also be used to manipulate GraphQL data server-side.
Example where GraphQL mutation is used can be found in:

- :class:`github.RepositoryDiscussion.RepositoryDiscussion` method ``add_comment``
- :class:`github.RepositoryDiscussionComment.RepositoryDiscussionComment` method ``edit``
- :class:`github.RepositoryDiscussionComment.RepositoryDiscussionComment` method ``delete``

GraphQL mutations can be sent to the Github GraphQL API via these methods:

- :func:`github.Requester.Requester.graphql_named_mutation`
- :func:`github.Requester.Requester.graphql_named_mutation_class`

Pagination
----------

An example where GraphQL results are provided through pagination can be found in :class:`github.Repository.Repository` method ``get_discussions``.

The response has to contain a GraphQL pagination object for :func:`github.PaginatedList.PaginatedList` to be able to paginate through the results::

    totalCount
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
