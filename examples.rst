Examples from the community
==============

These are examples submited by the community to ilustrate PyGithub in action.

These examples are intended to compliment the documentation by showing ways you could use pyGitHub. They are not intended to replace the reading the documentation.

If there is something which you found confusing when using pyGitHub please add an example to the docs/examples.rst file

Basic Examples
==============


Login using getpass and read a users repos
-----------------
::

    from github import Github

    import getpass

    # Authenticate to github.com and create PyGithub "Github" object
    username = raw_input("Github Username:")
    pw = getpass.getpass()
    g = Github(username, pw)

    # Use the PyGithub Github object g to do whatever you want,
    # for example, list all your own repos (user is whichever user authenticated)

    for repo in g.get_user().get_repos():
        print (repo.name)

Create repo for an orginization
-----------------
::
        
    import sys
    sys.path.append("./PyGithub");
    from github import Github

    import getpass
    import argparse


    from github import Github
    from github import GithubException

    parser = argparse.ArgumentParser(description='List all repos for an org')
    parser.add_argument('orgName',help='github Organization name')

    args = parser.parse_args()

    username = raw_input("Github Username:")
    pw = getpass.getpass()
    g = Github(username, pw)
    orgName = args.orgName

    try:
        org = g.get_organization(orgName)
    except GithubException as ghe:
        print(ghe)

    try:
        org.create_repo(
            "myNewRepo", # name -- string
            "My new repo, created using PyGithub", # description -- string
            "http://www.example.org", # homepage -- string
            True, # private -- bool
            True, # has_issues -- bool
            True, # has_wiki -- bool
            True, # has_downloads -- bool
            auto_init=True,
            gitignore_template="Python")

        # You could also set team_id= to something of type github.Team.Team

    except GithubException as ghe:
        print(ghe)



Pull Request Examples
==============

One thing to keep in mind when interacting with GitHub pull requests is that all pull requests are issues. A pull requst inherits from the issues class and can be interacted with as an issue.

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
The pull request class has a comments atribute, but those are not the comments that you are probably looking for when trying to read pull request comments.

To read the pull request comments that you see when clicking on a pull request in GitHub you need to open the pull request as an issue

::

    prAsIssue = repo.get_issue(pullRequest.number)
    comments  = prAsIssue.get_comments()                #these will be the comments on the pull request

Commenting on a pull request
-----------------

To add a comment to a pull request use the method for an issue

::

    prAsIssue.create_comment("the text of the comment")


Closing a pull request
-----------------

Similarly, to close a pull reqeust it needs to be opened as an issue also

::

    prAsIssue.edit(state='closed')


