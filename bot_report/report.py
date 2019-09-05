# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""
report.py

Generates report on Bot Framework issues.

See README.md for details on installing/using.

"""
import os
import sys
import copy
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

BYPASS_USERFILTER_REPOS = [
    'botbuilder-tools',
]

MICROSFT_EMPLOYEES=[
    'awalia13',
    'kumar2608',
    'bill7zz',
    'washingtonkayaker',
    'jonathanfingold',
    'automationteamva',
    'gasparacevedozainsouthworks',
]

DESCRIPTION_FILTER=[
    '[adaptive]'
]

BOT_SERVICES_LABEL = 'Bot Services'
CUSTOMER_REPORTED_LABEL = 'customer-reported'
SUPPORTABILITY_LABEL = 'supportability'
CUSTOMER_REPLIED_TO_LABEL = 'customer-replied-to'
fileName = "report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
outputFile = open(fileName, mode="w", encoding="utf-8")

def print_status(text):
    print(u''+text)
    if outputFile:
        outputFile.write(text + "\n")
            
def label_issue(issue):
    #print(f'LABEL: {issue.login}')
    bot_service_label = False   
    customer_reported = False
    supportability = False
    customer_replied_to = False
    for label in issue.labels:
        if label.name == BOT_SERVICES_LABEL:
            bot_service_label = True
        elif label.name == CUSTOMER_REPORTED_LABEL:
            customer_reported = True
        elif label.name == SUPPORTABILITY_LABEL:
            supportability = True
        elif label.name == CUSTOMER_REPLIED_TO_LABEL:
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

MILESTONE_LABELS=[
    '4.5',
    '4.6',
    '4.7',
    '4.8',
    'Backlog',
]
def filter_stale_customer_issues(issue, days_old=60):
    """Filter stale customer issues.
    Return True if it should filter the issue.
    """
    for label in issue.labels:
        if label.name in MILESTONE_LABELS:
            return True
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
    return [line.strip().lower() for line in members]

def filter_azure(repo, issue):
    if repo.lower() == 'azure/azure-cli':
        for label in issue.labels:
            if label.name == 'Bot Service':
                return False
        return True
    return False

def strfdelta(tdelta, fmt):
    """Utility function.  Formats a `timedelta` into human readable string."""
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def add_label(repo, issue, label_name):
    """Add a label to an issue."""
    try:
        a_label = repo.get_label(name=label_name)
        if label:
            print_status(f'        Adding label {label_name}')
            issue.add_to_labels(a_label)
            return True
    except Exception as ex:
        print_status(f'ERROR: Could not find label {label_name} in repo {repo.name}.  You have to go add it!', file=sys.stderr)
        raise ex

def print_issue(issue):
        print_status(f'        {issue.number} : {issue.title}')
        print_status(f'             {issue.html_url}')
        # Uncomment if you want to add labels.
        # add_label(repo, issue, BOT_SERVICES_LABEL)

def print_stale_issue(issue, employee_last_touch=True):
    comments_paged = issue.get_comments()
    comment = [msg for msg in comments_paged][-1]
    assert(comment)
    last_touch_by_microsoft = comment.user.login.strip().lower() in MEMBERS
    if employee_last_touch == last_touch_by_microsoft:
        print_status(f'         {issue.number} : {issue.title}')
        print_status(f'            Issue Age: {Fore.RED}{strfdelta(datetime.utcnow() - issue.created_at, "{days} days {hours}:{minutes}:{seconds}")}{Style.RESET_ALL}')
        print_status(f'            Last Comment: {Fore.RED}{strfdelta(datetime.utcnow() - issue.last_comment, "{days} days {hours}:{minutes}:{seconds}")}{Style.RESET_ALL}')
        print_status(f'                 {issue.html_url}')

def add_last_comment(issue, stale_days=10):
    """Takes an issue, adds the last comment time.
    Filters items, where the last comment is not at least stale_days old.
    Returns a copy of the issue.
    """
    comments_paged = issue.get_comments()
    if (comments_paged.totalCount == 0):
       return None
    last_comment = ([msg for msg in comments_paged] or [None])[-1]
    assert(last_comment)
    if last_comment.created_at > (datetime.utcnow() - timedelta(days=stale_days)):
        # Filter items.
        return None
    result = copy.copy(issue)
    result.last_comment = last_comment.created_at
    return result

START_DATE = datetime(2019, 7, 1, 0, 0)

print_status('Bot Framework SDK Github Report')
print_status('===============================')

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

MEMBERS = get_msorg_members(g) + MICROSFT_EMPLOYEES

for repo in REPOS:
    repo_name = repo if '/' in repo else f'microsoft/{repo}'
    repo = g.get_repo(repo_name)

    # Set state='closed' to find closed issues that weren't tagged properly
    # Note: repo.get_issues() underlying library appears to have a bug where
    # `start` and `labels` don't seem to work properly, so we do it manually here.
    # Super inefficient on the wire!
    open_issues = [issue for issue in repo.get_issues(state='open')\
        if issue.created_at >= START_DATE and not filter_azure(repo_name, issue)]
    print_status(f'Repo: {repo.full_name}:')
    print_status(f'   Total open issues after {START_DATE} : {len(open_issues)}')

    if (repo.name in BYPASS_USERFILTER_REPOS):
        user_filtered_issues = open_issues
    else:
        user_filtered_issues = [issue for issue in open_issues if (not issue.user.login.strip().lower() in MEMBERS and not issue.pull_request)]

    if repo_name.lower() != 'azure/azure-cli':
        no_bs_label = [issue for issue in user_filtered_issues if not filter_bot_service_label(issue)]
        if no_bs_label:
            print_status(f'   No "Bot Services": Count: {len(no_bs_label)}')
            for issue in no_bs_label:
                print_issue(issue)

        no_cr_label = [issue for issue in user_filtered_issues if not filter_customer_reported_label(issue)]
        if no_cr_label:
            print_status(f'   No "Customer Reported": Count: {len(no_cr_label)}')
            for issue in no_cr_label:
                print_issue(issue)

        no_crt_label = [issue for issue in user_filtered_issues if not filter_customer_replied_label(issue)]
        if no_crt_label:
            print_status(f'   No "Customer Replied": Count: {len(no_crt_label)}')
            for issue in no_crt_label:
                print_issue(issue)

        stale_days = 10
        stale_customer_issues = [add_last_comment(issue, stale_days) for issue in user_filtered_issues if not filter_stale_customer_issues(issue, days_old=stale_days)]
        stale_no_nones = [i for i in stale_customer_issues if i]
        stale_descending = sorted(stale_no_nones, key=lambda issue: issue.last_comment, reverse=False)
        if stale_descending:
            print_status(f'   90-day stale : Customer issues not touched in more than {stale_days} days: Count: {len(stale_descending)}')
            print_status(f'      Last touched by {Fore.GREEN}CUSTOMER{Style.RESET_ALL}:')
            for issue in stale_descending:
                print_stale_issue(issue, employee_last_touch=False)
            print_status(f'      Last touched by {Fore.GREEN}MICROSOFT{Style.RESET_ALL}:')
            for issue in stale_descending:
                print_stale_issue(issue, employee_last_touch=True)
    else:
        for issue in user_filtered_issues:
            print_status(f'        {issue.number} : {issue.title}')
            print_status(f'             {issue.html_url}')


outputFile.close()
os.system("notepad " + fileName)