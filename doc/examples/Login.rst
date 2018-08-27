Login
======

Basic login demo
--------------------------

.. code-block:: python

    from github import Github

    g = Github("user", "password")

    repo =  g.get_user().get_repo('test-repo')
    for issue in repo.get_issues(): 
        print(issue.title)
