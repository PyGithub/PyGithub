# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
report.py

Generates report on Bot Framework issues.

See README.md for details on installing/using.

"""
import os
import sys
import requests
from github import Github, Label, GithubObject
from colorama import Fore, Style, init
from datetime import datetime, timedelta

HOW_TO_SET_CREDS = """
To set your Git credentials, you can use personal access token (preferred) or 
username password.

To use a personal token (preferred):
    Go to https://github.com/settings/tokens
    Click on "Generate new token"
     - Give note like "SDK tool"
     - Check the repo (and everything underneath)
     - Copy the token value (and store in safe place).
    On command line:
      Windows: set GIT_PERSONAL_TOKEN=<your token>
      Powershell: $env:GIT_PERSONAL_TOKEN="<your token>" (Note the quotes)
      Linux: export GIT_PERSONAL_TOKEN=<your token>

To use username and password, on the command line:
  Windows: set GIT_NAME=<your git username> 
           set GIT_PW=<your git pw>
  Powershell: $env:GIT_NAME = "<your git username>" (Note the quotes)
              $env:GIT_PW = "<your git pw>"
  Linux: export GIT_NAME=<your git username> 
         export GIT_PW=<your git pw>
"""
init(convert=True)
GIT_NAME = os.getenv('GIT_NAME')
GIT_PW = os.getenv('GIT_PW')
GIT_PERSONAL_TOKEN = os.getenv('GIT_PERSONAL_TOKEN')

if not GIT_NAME or not GIT_PW:
    if not GIT_PERSONAL_TOKEN:
        print(Fore.RED + '\nYour GIT CREDENTIALS are not set!!\n' + Style.RESET_ALL)
        print(HOW_TO_SET_CREDS)
        sys.exit(2)

REPOS = [
    'BotFramework-DirectLine-DotNet',
    'BotFramework-Composer',
    'BotFramework-Services',
    'BotBuilder-V3',
    'BotFramework-sdk',
    'botbuilder-dotnet',
    'botbuilder-js',
    'botbuilder-python',
    'botbuilder-java',
    'botbuilder-samples',
    'botframework-emulator',
    'botframework-webchat',
    'botbuilder-tools',
    'botframework-directlinejs',
    'botframework-cli',
    'azure/azure-cli',
]

def label_issue(issue):
    bot_service_label = False
    customer_reported = False
    supportability = False
    customer_replied_to = False
    for label in issue.labels:
        if label.name == 'Bot Services':
            bot_service_label = True
        elif label.name == 'customer-reported':
            customer_reported = True
        elif label.name == 'supportability':
            supportability = True
        elif label.name == 'customer-replied-to':
            customer_replied_to = True
    return bot_service_label, customer_reported, supportability, customer_replied_to

def filter_bot_service_label(issue):
    bs, cr, s, crt = label_issue(issue)
    return bs

def filter_customer_reported_label(issue):
    bs, cr, s, crt = label_issue(issue)
    return cr

def filter_customer_replied_label(issue):
    bs, cr, s, crt = label_issue(issue)
    return crt

def filter_stale_customer_issues(issue, days_old=60):
    return not issue.created_at + timedelta(days=days_old) < datetime.now()

def get_msorg_members(github, refresh_in_days=5):
    """Get members of the Microsoft github organization.
    This is cached in the `members.txt` file.
    If it gets stale (over `refresh_in_days` old), then refresh it.
    """

    # See if we need to refresh the cache
    members_fname = './members-do-not-check-in.txt'

    member_updated = datetime.fromtimestamp(os.path.getmtime(members_fname))\
        if os.path.exists(members_fname) else datetime.min
    if datetime.now() - timedelta(days=refresh_in_days) > member_updated:
        print('Your members cache is out of date.  Refreshing.. (Could take several minutes)')
        ms_org = github.get_organization('microsoft')
        members = ms_org.get_members()
        with open(members_fname, 'w') as member_file:
            for member in members:
                member_file.write(f'{member.login}\n')
    with open(members_fname, 'r') as member_file:
        members = member_file.readlines()
    return [line.strip() for line in members]

def filter_azure(repo, issue):
    if repo == 'azure-cli':
        for label in issue.labels:
            if label.name == 'Bot Service':
                return True
    return False

def strfdelta(tdelta, fmt):
    """Utility function.  Formats a `timedelta` into human readable string."""
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

START_DATE = datetime(2019, 7, 1, 0, 0)

print('Bot Framework SDK Github Report')
print('===============================')
g = None
if GIT_PERSONAL_TOKEN:
    g = Github(GIT_PERSONAL_TOKEN)
else:
    print('Retrieving items from Github requires two-factor authentication.')
    print('Using your phones authenticator app, type in the latest code. ')
    print('(ie, https://www.microsoft.com/en-us/account/authenticator)')
    print(Fore.RED + 'You will need to refresh your token a few times during the run.' + Style.RESET_ALL)
    otp = input('   Enter code with no spaces (ie, `123456`):')
    print(Style.RESET_ALL)
    g = Github(GIT_NAME, GIT_PW, otp=str(otp))

MEMBERS = get_msorg_members(g)

for repo in REPOS:
    repo_name = repo if '/' in repo else f'microsoft/{repo}'
    repo = g.get_repo(repo_name)

    # BUGBUG: repo.getissues should be fixed- accepts start and labels as parms
    # but not working.
    open_issues = [issue for issue in repo.get_issues(state='open')\
        if issue.created_at >= START_DATE and filter_azure(repo, issue)]
    print(f'Repo: {repo.full_name}:')
    print(f'   Total issues after {START_DATE} : {len(open_issues)}')

    user_filtered_issues = [issue for issue in open_issues if not issue.user.login.strip() in MEMBERS and not issue.pull_request]

    no_bs_label = [issue for issue in user_filtered_issues if not filter_bot_service_label(issue)]
    print(f'   No "Bot Services": Count: {len(no_bs_label)}')
    for issue in no_bs_label:
        print(f'        {issue.id} : {issue.title}')
        print(f'             {issue.html_url}')

    no_cr_label = [issue for issue in user_filtered_issues if not filter_customer_reported_label(issue)]
    print(f'   No "Customer Reported": Count: {len(no_cr_label)}')
    for issue in no_cr_label:
        print(f'        {issue.id} : {issue.title}')
        print(f'             {issue.html_url}')

    no_crt_label = [issue for issue in user_filtered_issues if not filter_customer_replied_label(issue)]
    print(f'   No "Customer Replied": Count: {len(no_crt_label)}')
    for issue in no_crt_label:
        print(f'        {issue.id} : {issue.title}')
        print(f'             {issue.html_url}')

    stale_days = 60
    stale_customer_issues = [issue for issue in user_filtered_issues if not filter_stale_customer_issues(issue, days_old=stale_days)]
    print(f'   90-day stale : Customer issues older than {stale_days} days: {len(stale_customer_issues)}')
    for issue in stale_customer_issues:
        print(f'        {issue.id} : {issue.title}')
        print(f'        {Fore.RED}{strfdelta(datetime.now() - issue.created_at, "{days} days {hours}:{minutes}:{seconds}")}{Style.RESET_ALL}')
        print(f'             {issue.html_url}')

