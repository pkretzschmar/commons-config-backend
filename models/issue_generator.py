import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

from models.data.issue_submission_data import test_issue_data


load_dotenv() 

class IssueGeneratorModel:
    def __init__(self,
                 title=None,
                 token_lockup=None):
        self.title = title if title is not None else "TEC Config Dashboard Proposal"
        self.token_lockup = token_lockup if title is not None else {}

    def generate_output(self):
        PARAMS_BOT_AUTH_TOKEN = os.getenv("PARAMS_BOT_AUTH_TOKEN")
        headers = {'Content-Type': 'application/json', 'Authorization': PARAMS_BOT_AUTH_TOKEN}
        data = {"title": self.title, "body": test_issue_data}
        r = requests.post('https://api.github.com/repos/CommonsBuild/test-issues-config-dashboard/issues', data=json.dumps(data), headers=headers)
        return r.text
