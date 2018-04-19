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

Commenting on a pull request
-----------------

To add a comment to a pull request use the method for an issue

::

    prAsIssue.create_comment(commentText)

Checking pull request comments
-----------------
The pull request class has a comments atribute, but those are not the comments that you are probably looking for when trying to read pull request comments.

To read the pull request comments that you see when clicking on a pull request in GitHub you need to open the pull request as an issue

::

    prAsIssue = repo.get_issue(pullRequest.number)
    comments  = prAsIssue.get_comments()                #these will be the comments on the pull request

Closing a pull request
-----------------

Similarly, to close a pull reqeust it needs to be opened as an issue also

::

    prAsIssue.edit(state='closed')


