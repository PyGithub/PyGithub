# Git Stats for Bot Framework

Simple command line tool to check what the stats are on Bot Framework SDK repos.

Requires Python.

Currently performs the following (for all the repos we currently manage):
- Filters out Microsoft employees or vendors
- Count of  **total issues** after `7/1/1019` (when we started tracking).
- Issues that don't contain the **`Bot Services`** label.
- Issues that don't contain the **`customer-reported`** label.
- Issues that don't contain the  **`customer-replied-to`** label.


### Clone repo
```bash
git clone https://github.com/daveta/PyGithub.git
```
### Install local package
```bash
cd PyGithub
pip install -e .
```
### Set your git creds
To set your Git credentials, in the command line type:
```bash
set GIT_NAME=<your git username>
set GIT_PW=<your git pw>
```
Alternatively if you are in Powershell:
```bash
$env:GIT_NAME = "<your git username>"
$env:GIT_PW = "<your git pw>"
```
Alternatively in linux:
```bash
export GIT_NAME="<your git username>"
export GIT_PW="<your git pw>"
```

### Run
```bash
cd bot_report
python report.py
```

Sample Output:
```bash
PS D:\python\github\PyGithub\bot_report> python report.py
Bot Framework SDK Github Report
===============================
Retrieving items from Github requires two-factor authentication.
Using your phones authenticator app, type in the latest code.   
(ie, https://www.microsoft.com/en-us/account/authenticator)     
You will need to refresh your token a few times during the run. 
   Enter code with no spaces (ie, `123456`):597450

Repo: microsoft/botframework-sdk:
   Total issues after 2019-07-01 00:00:00 : 23
   No "Bot Services": Count: 1
        482345966 : Universal Bot Authentification in multple Channels (MS Teams, Web Bot, Bot Emulator)
             https://github.com/microsoft/botframework-sdk/issues/5496
   No "Customer Reported": Count: 1
        482345966 : Universal Bot Authentification in multple Channels (MS Teams, Web Bot, Bot Emulator) 
             https://github.com/microsoft/botframework-sdk/issues/5496
   No "Customer Replied": Count: 2
        482345966 : Universal Bot Authentification in multple Channels (MS Teams, Web Bot, Bot Emulator)
             https://github.com/microsoft/botframework-sdk/issues/5496
Repo: microsoft/botbuilder-dotnet:
   Total issues after 2019-07-01 00:00:00 : 77
   No "Bot Services": Count: 7
        483155976 : cannot use safe JSON deserialization for Dialog State object
             https://github.com/microsoft/botbuilder-dotnet/issues/2437
        481374209 : TwilioHelper.GetMessageAttachments doesn't bounds check
             https://github.com/microsoft/botbuilder-dotnet/issues/2416
        479889798 : DialogManager RootDialog property setter has bad side effects
             https://github.com/microsoft/botbuilder-dotnet/issues/2400
        479494855 : [Adaptive] Break and Continue can be added to ForEach step
             https://github.com/microsoft/botbuilder-dotnet/issues/2394
        477877794 : [Adaptive][Expressions] Sort and Search should be supported in the next version
             https://github.com/microsoft/botbuilder-dotnet/issues/2380
        476816201 : add Support Adaptive Card Version function
             https://github.com/microsoft/botbuilder-dotnet/issues/2370
        472137078 : [Adaptive] [Expression] language requires quotes to represent string literals including empty strings
             https://github.com/microsoft/botbuilder-dotnet/issues/2308
```
