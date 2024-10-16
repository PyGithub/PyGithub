from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
import os
os.environ["GITHUB_TOKEN"]
auth = Auth.Token(os.environ["GITHUB_TOKEN"])

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", auth=auth)

from github.Package import PackageType

for _ in g.get_user().get_packages(PackageType.CONTAINER):
    print(_)
    for version in _.get_versions():
        print(version)
        print(version.name)
        print(version.id)
        print(version.url)
        print(version.package_html_url)
        print(version.license)
        print(version.created_at)
        print(version.updated_at)
        print(version.metadata)
        print(version.html_url)
        

