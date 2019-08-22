# Git Stats for Bot Framework

Simple command line tool to check what the stats are on Bot Framework SDK repos.

Requires Python.

Currently performs the following (for all the repos we currently manage):
- Filters out Microsoft employees or vendors
- Count of  **total issues** after `7/1/1019` (when we started tracking).
- Issues that don't contain the **`Bot Services`** label.
- Issues that don't contain the **`customer-reported`** label.
- Issues that don't contain the  **`customer-replied-to`** label.
- Issues that are endanger of not being closed within 90 days.


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
To set your Git credentials, you can use personal access token (preferred) or 
username password.

- To use a personal token (**recommended**):

    - Go to https://github.com/settings/tokens
    - Click on "Generate new token"
      - Give note like "SDK tool"
      - Check the "`repo`" check box (and all items underneath)
      - Copy the token value (don't worry you can regen if you forget it)
     - On command line:
              Windows: `set GIT_PERSONAL_TOKEN=<your token>`
              Powershell: `$env:GIT_PERSONAL_TOKEN="<your token>"` (Note the quotes)
              Linux: `export GIT_PERSONAL_TOKEN=<your token>`
    
- To use username and password, on the command line:
    - Windows: 
    ```bash
    set GIT_NAME=<your git username>
    set GIT_PW=<your git pw>
    ```
    - Powershell: 
    ```bash
    $env:GIT_NAME = "<your git username>" # (Note the quotes)
    $env:GIT_PW = "<your git pw>"
    ```

    - Linux:
    ```bash
    export GIT_NAME=<your git username>
    export GIT_PW=<your git pw>
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
Note: Azure-cli commented out at the moment.
Repo: microsoft/BotFramework-DirectLine-DotNet:
   Total issues after 2019-07-01 00:00:00 : 0
   No "Bot Services": Count: 0
   No "Customer Reported": Count: 0
   No "Customer Replied": Count: 0
   90-day stale : Customer issues older than 60 days: 0
Repo: microsoft/BotFramework-Composer:
   Total issues after 2019-07-01 00:00:00 : 76
   No "Bot Services": Count: 0
   No "Customer Reported": Count: 0
   No "Customer Replied": Count: 0
   90-day stale : Customer issues older than 60 days: 0
...
```
