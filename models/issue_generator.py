import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

from data.issue_submission_data import test_issue_data


load_dotenv() 

class IssueGeneratorModel:
    def __init__(self,
                 title=None,
                 token_lockup=None,
                 abc=None,
                 tao_voting=None,
                 conviction_voting=None,
                 advanced_settings=None):
        self.title = title if title is not None else "TEC Config Dashboard Proposal test"
        self.token_lockup = token_lockup if token_lockup is not None else {
            "opening_price": 5,
            "token_freeze": 20,
            "token_thaw": 15
        }
        self.abc = abc if abc is not None else {
            "commons_tribute": 25,
            "entry_tribute": 5,
            "exit_tribute": 15
        }
        self.tao_voting = tao_voting if tao_voting is not None else {
            "support_required": 40,
            "minimum_quorum": 10,
            "vote_duration": 7,
            "delegated_voting_period": 3,
            "quiet_ending_period": 2,
            "quiet_ending_extension": 1,
            "execution_delay": 1
        }
        self.conviction_voting = conviction_voting if conviction_voting is not None else {
            "conviction_growth": 2,
            "minimum_conviction": 1,
            "relative_spending_limit": 20
        }
        self.advanced_settings = advanced_settings if advanced_settings is not None else {
            "minimum_effective_supply": 4,
            "hatchers_rage_quit": 3,
            "virtual_balance": 3_000_000
        }

    def format_output_issue(self):
        formated_output = test_issue_data.format(
            token_freeze_period=self.token_lockup.get("token_freeze", ""),
            token_thaw_period=self.token_lockup.get("token_thaw", ""),
            opening_price=self.token_lockup.get("opening_price", ""),

            commons_tribute=self.abc.get("commons_tribute", ""),
            commons_tribute_remainder= 100 - self.abc.get("commons_tribute", ""),
            entry_tribute=self.abc.get("entry_tribute", ""),
            exit_tribute=self.abc.get("exit_tribute", ""),
            support_required=self.tao_voting.get("support_required", ""),
            minimum_quorum=self.tao_voting.get("minimum_quorum", ""),

            vote_duration_days=self.tao_voting.get("vote_duration", ""),
            delegated_voting_days=self.tao_voting.get("delegated_voting_period", ""),
            quiet_ending_days=self.tao_voting.get("quiet_ending_period", ""),
            quiet_ending_extension_days=self.tao_voting.get("quiet_ending_extension", ""),
            execution_delay_hours=self.tao_voting.get("execution_delay", ""),

            conviction_growth_days=self.conviction_voting.get("conviction_growth", ""),
            minimum_conviction=self.conviction_voting.get("minimum_conviction", ""),
            relative_spending_limit=self.conviction_voting.get("relative_spending_limit", ""),
        
            minimum_effective_supply=self.advanced_settings.get("minimum_effective_supply", ""),
            hatchers_rage_quit=self.advanced_settings.get("hatchers_rage_quit", ""),
            virtual_balance="{:,}".format(self.advanced_settings.get("virtual_balance", ""))

        )
        return formated_output

    def generate_output(self):
        PARAMS_BOT_AUTH_TOKEN = os.getenv("PARAMS_BOT_AUTH_TOKEN")
        headers = {'Content-Type': 'application/json', 'Authorization': PARAMS_BOT_AUTH_TOKEN}
        data = {"title": self.title, "body": self.format_output_issue()}
        r = requests.post('https://api.github.com/repos/CommonsBuild/test-issues-config-dashboard/issues', data=json.dumps(data), headers=headers)
        return r.text
