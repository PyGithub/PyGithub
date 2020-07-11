PullRequest
===========

Create a new Pull Request
-------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> body = '''
    >>> SUMMARY
    >>> Change HTTP library used to send requests
    >>>
    >>> TESTS
    >>>   - [x] Send 'GET' request
    >>>   - [x] Send 'POST' request with/without body
    >>> '''
    >>> pr = repo.create_pull(title="Use 'requests' instead of 'httplib'", body=body, head="develop", base="master")
    >>> pr
    PullRequest(title="Use 'requests' instead of 'httplib'", number=664)

Get Pull Request by Number
---------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> pr = repo.get_pull(664)
    >>> pr
    PullRequest(title="Use 'requests' instead of 'httplib'", number=664)

Get Pull Requests by Query
--------------------------

.. code-block:: python

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> pulls = repo.get_pulls(state='open', sort='created', base='master') 
    >>> for pr in pulls:
    ...    print(pr.number)
    ... 
    400
    861
    875
    876
