import os

from github import Github
from github import GithubObject

# Get environment variables
ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')

print(os.getenv('GITHUB_TOKEN'))


g = Github(ACCESS_TOKEN)

organization = g.get_organization("Mck-Internal-Test")
template_repo = g.get_repo("Mck-Internal-Test/TemplateRepo")
new_repo_name = "APIHelloWorld2"
repo_description = "This is your first repository"

private = True
try:
    organization.create_repo_from_template(organization.login, new_repo_name, template_repo.name, repo_description,
                                           private)
except:
    print(" Repo Name already exists on this account")
