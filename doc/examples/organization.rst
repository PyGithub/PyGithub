
Organization
==========

Get repository's in organization

.. code-block:: python

	>>>git = Github(access_token)
	>>>org = git.get_organization("PyGithub")
	>>>repository  = org.get_repos()
	>>>for repos in repository:
		print(repos)

	Repository(full_name="PyGithub/PyGithub")


Get all members of an organization without a role filter


.. code-block:: python
	
	>>>git = Github(access_token)
	>>>org = git.get_organization("PyGithub")
	>>>membership = org.get_members()
	>>>for members in membership:
		print(members)
	   NamedUser(login="adamtheturtle")
	   NamedUser(login="jacquev6")
	   NamedUser(login="JPWKU")
           NamedUser(login="sfdye")


Get all members of an organization with role filter

.. code-block:: python
	>>>git = Github(access_token)
	>>>org = git.get_organization("PyGithub")
	>>>membership = org.get_members('Owner')
	>>>for members in membership:
		print(members)
	
	   NamedUser(login="adamtheturtle")
	   NamedUser(login="jacquev6")
	   NamedUser(login="JPWKU")
           NamedUser(login="sfdye")
