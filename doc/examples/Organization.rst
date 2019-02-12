
Organization
==========

Get repository's in an organization

.. code-block:: python

	>>> git = Github(access_token)
	>>> org = git.get_organization("PyGithub")
	>>> repository = org.get_repos()
	>>> for repos in repository:
	...	print(repos)
	...
	Repository(full_name="PyGithub/PyGithub")


Get all members of an organization. 


.. code-block:: python
	
	>>> git = Github(access_token)
	>>> org = git.get_organization("PyGithub")
	>>> membership = org.get_members()
	>>> for members in membership:
	   ...	print(members)
		
	   ...	
	   NamedUser(login="adamtheturtle")
	   NamedUser(login="jacquev6")
	   NamedUser(login="JPWKU")
           NamedUser(login="sfdye")


Get members of an organization by certain role

.. code-block:: python
	
	>>> git = Github(access_token)
	>>> org = git.get_organization("PyGithub")
	>>> membership = org.get_members('Owner')
	>>> for members in membership:
	   ...	print(members)
           
	   ...
	   NamedUser(login="adamtheturtle")
	   NamedUser(login="jacquev6")
	   NamedUser(login="JPWKU")
           NamedUser(login="sfdye")
