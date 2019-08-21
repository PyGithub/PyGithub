# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
report.py

Generates report on Bot Framework issues.


Install:
  $ pip install -e .

To Use:
  python bot_report/sdk_reporting.py

"""
import os
import sys
import requests
from github import Github
from colorama import Fore, Style, init
import datetime

HOW_TO_SET_CREDS = """
To set your Git credentials, in the command line type:
  set GIT_NAME=<your git username> 
  set GIT_PW=<your git pw>

Alternatively if you are in Powershell:
  $env:GIT_NAME = "<your git username>"
  $env:GIT_PW = "<your git pw>"
"""
init(convert=True)
GIT_NAME = os.getenv('GIT_NAME')
GIT_PW = os.getenv('GIT_PW')
if not GIT_NAME or not GIT_PW:
    print(Fore.RED + '\nYour GIT CREDENTIALS are not set!!\n' + Style.RESET_ALL)
    print(HOW_TO_SET_CREDS)
    sys.exit(2)


REPOS = [
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
    'botframework-composer',
    'botframework-services',
    'botframework-directline-dotnet',
    'botbuilder-v3',
]

MICROSOFT_COMPANY_ALIASES = [
    'Microsoft',
    'MS',
    '@howdyai',
    '@Microsoft',
    'FUSE Labs - Microsoft',
    'SOUTHWORKS',
    '@microsoft',
]

MICROSOFT_PEOPLE = [
    'JonathanFingold',
    'BruceHaley',
]

def filter_user(user, debug=False):
    if user.company:
        company = user.company.strip()
        if company in MICROSOFT_COMPANY_ALIASES:
            if debug:
                print(f'User {user.name} filtered on company: {user.company}')
            return True
    if user.email and user.email.endswith('microsoft.com'):
        if debug:
            print(f'User {user.name} filtered on email: {user.email}')
        return True
    return False

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

START_DATE = datetime.datetime(2019, 7, 1, 0, 0)


print('Bot Framework SDK Github Report')
print('===============================')
print('Retrieving items from Github requires two-factor authentication.')
print('Using your phones authenticator app, type in the latest code. ')
print('(ie, https://www.microsoft.com/en-us/account/authenticator)')
print(Fore.RED + 'You will need to refresh your token a few times during the run.' + Style.RESET_ALL)
otp = input('   Enter code with no spaces (ie, `123456`):')
print(Style.RESET_ALL)
g = Github(GIT_NAME, GIT_PW, otp=otp)
for repo in REPOS:
    repo_name = repo if '/' in repo else f'Microsoft/{repo}'
    repo = g.get_repo(repo_name)
    open_issues = [issue for issue in repo.get_issues(state='open') \
        if issue.created_at >= START_DATE]
    print(f'Repo: {repo.full_name}:')
    print(f'   Total issues after {START_DATE} : {len(open_issues)}')

    user_filtered_issues = [issue for issue in open_issues if not filter_user(issue.user) and not issue.pull_request]

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
    for issue in no_cr_label:
        print(f'        {issue.id} : {issue.title}')
        print(f'             {issue.html_url}')
