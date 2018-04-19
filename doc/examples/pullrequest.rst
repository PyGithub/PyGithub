Pull Request Examples
==============

One thing to keep in mind when interacting with GitHub pull requests is that all pull requests are issues. That is a pull requst inherits from the issues class and can be interacted with as an issue.

Getting a list of all pull requests open for an originization
-----------------

::

    from github     import Github
    g       = Github('yourusername', 'yourpassword')    #login
    org     = g.get_organization('orgName')             #get an orginization
    repos   = org.get_repos()                           #get all the repos in that orginization
    for repo in repos:
        openPullRequests = repo.get_pulls()             #a list of all pull requests open in that repository

Checking pull request comments
-----------------


Closing a pull request
-----------------
