Examples from the community
==============

These are examples submited by the community to illustrate PyGithub in action.

These examples are intended to compliment the documentation by showing ways you could use pyGitHub. They are not intended to replace reading the documentation.

Please add your own example(s) to the docs/examples.rst file to help the pyGitHub community!

Basic Examples
==============

Accessing the API endpoints with your GitHub API key
----------------------------------------------------
::

First, obtain your GitHub API key while logged in by going to Settings --> Developer Settings --> Personal Access Tokens --> Generate New Token (button). Give your token a name, select the scope required for your use case, and click the green "Generate Token" button at the bottom of the page.

Copy your new token but DO NOT put it anywhere yet, and especially don't commit it!

(1) Create a file in your main project directory called ``.gitignore``. This file tells git what it should NOT commit (ie: what it can ignore). You should never commit your API key, so we're going to store the API key in a separate file,  list **that** file in ``.gitignore``, and then commit ``.gitignore`` instead of the file that has your API key in it. The name of this "storage" file is ``secrets.sh``, so add the text ``secrets.sh`` to ``.gitignore``. Commit ``.gitignore``.

(2) Now, create a file in your main project directory and name it ``secrets.sh``. Type this line into ``secrets.sh``, pasting in your GitHub API key as a string where specified:

    ``export GITHUB_API_KEY='yourkeygoeshere'``
    
    If you run ``git status`` at this point you'll see that ``secrets.sh`` does not appear in the output. It's safely hiding inside ``.gitignore``.
    
(3) In your Terminal -- and you're inside an environment, right? -- run ``source secrets.sh``. This will make your GitHub API key visible to your computer.

(4) Next, create a new file in your project directory that will hold your code. In this example we'll call it ``try_pygithub.py``. Copy and paste this code into ``try_pygithub.py``. Be sure to read the explanation that follows.

.. codeblock:: python
    from github import Github
    import os

    GITHUB_API_KEY = os.environ['GITHUB_API_KEY']
    g = Github(GITHUB_API_KEY)
        
In the code snippet above, we import the ``Github`` class from pyGitHub and also import Python's ``os`` package. The ``os`` package gives us a way to pull in the GitHub API key that the computer can now see after sourcing ``secrets.sh``. We then pass the API key in as an argument when creating a new ``Github`` instance called ``g``. From here, we can call `any of the methods that are associated with the Github object <http://pygithub.readthedocs.io/en/latest/github.html>`_ on **our** instance, ``g``. For example, we can call `the get_user() method <http://pygithub.readthedocs.io/en/latest/github.html#github.MainClass.Github.get_user>`_ which returns a `NamedUser object <http://pygithub.readthedocs.io/en/latest/github_objects/NamedUser.html#github.NamedUser.NamedUser>`_, which itself gives us access to attributes like the user's avatar URL, bio, company, email, etc.

.. codeblock:: python

    # Continued from previous code
    def get_email():
        user = g.get_user('allardbrain')
        user_url = user.url
        print(user_url)

        return

Login using getpass and read a user's repos
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
        repo = org.create_repo(
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
        
        repo.create_file("/FILENAME.md", "commit description", "This is the text which will show up in the file")
        
    except GithubException as ghe:
        print(ghe)


Working with a repo's code using the ContentFile class
======================================================



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


