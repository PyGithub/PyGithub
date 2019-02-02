
Organization
==========

Get repository's in organizations

.. code-block:: python

	>>>git = Github(access_token)
	>>>org = git.get_organization("python-sg")
	>>>repository  = org.get_repos()
	>>>for repos in repository:
		print(repos)

	Repository(full_name="PyGithub/PyGithub")
