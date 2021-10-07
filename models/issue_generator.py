import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

from models.data.issue_submission_data import test_issue_data
from models.token_lockup import TokenLockupModel
from models.conviction_voting import ConvictionVotingModel
from models.augmented_bonding_curve import BondingCurveHandler

load_dotenv() 

class IssueGeneratorModel:
    def __init__(self,
                 title=None,
                 token_lockup=None,
                 abc=None,
                 tao_voting=None,
                 conviction_voting=None,
                 advanced_settings=None,
                 overall_strategy=None):
        self.title = title if title is not None else "TEC Config Dashboard Proposal test"
        self.overall_strategy = overall_strategy if overall_strategy is not None else ""
        self.token_lockup = token_lockup if token_lockup is not None else {
            "openingPrice": 5,
            "tokenFreeze": 20,
            "tokenThaw": 15,
            "strategy": ""
        }
        self.abc = abc if abc is not None else {
            "commonsTribute": 0.25,
            "ragequitAmount": 60,
            "initialBuy": 200,
            "openingPrice":1.65,
            "reserveBalance": 1571.22357,
            "entryTribute": 0.05,
            "exitTribute": 0.15,
            "hatchScenarioFunding": 1571.22357,
            "stepList": [[5000, "wxDai"], [100000, "wxDai"], [3000, "TEC"]],
            "zoomGraph": 0,
            "strategy": ""
        }
        self.tao_voting = tao_voting if tao_voting is not None else {
            "supportRequired": 40,
            "minimumQuorum": 10,
            "voteDuration": 7,
            "delegatedVotingPeriod": 3,
            "quietEndingPeriod": 2,
            "quietEndingExtension": 1,
            "executionDelay": 1,
            "strategy": ""
        }
        self.conviction_voting = conviction_voting if conviction_voting is not None else {
            "convictionGrowth": 2,
            "minimumConviction": 0.01,
            "votingPeriodDays": 7,
            "spendingLimit": 0.2,
            "strategy": ""
        }
        self.advanced_settings = advanced_settings if advanced_settings is not None else {
            "minimumEffectiveSupply": 4,
            "hatchersRageQuit": 3,
            "virtualBalance": 3_000_000,
        }

    def format_output_issue(self):
        token_lockup_model = TokenLockupModel(
            opening_price=self.token_lockup.get("openingPrice", ""),
            token_freeze_period=self.token_lockup.get("tokenFreeze", ""),
            token_thaw_period=self.token_lockup.get("tokenThaw", ""),
        )
        token_lockup_output = token_lockup_model.get_data().get("output", "")
        token_lockup_table = token_lockup_output.get("table", "")

        augmented_bonding_curve_model = BondingCurveHandler(
                        commons_percentage=self.abc.get("commonsTribute", ""),
                        ragequit_amount=self.abc.get("ragequitAmount", ""),
                        opening_price=self.abc.get("openingPrice", ""),
                        entry_tribute=self.abc.get("entryTribute", ""),
                        exit_tribute=self.abc.get("exitTribute", ""),
                        scenario_reserve_balance=self.abc.get("reserveBalance", ""),
                        initial_buy=self.abc.get("initialBuy", ""),
                        steplist=self.abc.get("stepList", ""),
                        zoom_graph= self.abc.get("zoomGraph", ""))
        augmented_bonding_curve_output = augmented_bonding_curve_model.get_data()

        conviction_voting_model = ConvictionVotingModel(
            conviction_growth=self.conviction_voting.get("convictionGrowth", ""),
            minimum_conviction=self.conviction_voting.get("minimumConviction", ""),
            voting_period_days=self.conviction_voting.get("votingPeriodDays", ""),
            spending_limit=self.conviction_voting.get("spendingLimit", ""),
        )
        conviction_voting_output = conviction_voting_model.get_data().get("output", "")
        conviction_voting_table = conviction_voting_output.get("table", "")

        formated_output = test_issue_data.format(
            overall_strategy=self.overall_strategy,

            token_lockup_strategy=self.token_lockup.get("strategy", ""),
            token_freeze_period=self.token_lockup.get("tokenFreeze", ""),
            token_thaw_period=self.token_lockup.get("tokenThaw", ""),
            opening_price=self.token_lockup.get("openingPrice", ""),
            token_lockup_week=token_lockup_table["week"],
            tokens_released=["{0:.2f}".format(100 * item) for item in token_lockup_table["tokensReleased"]],
            price_floor=["{0:.2f}".format(item) for item in token_lockup_table["price"]],

            abc_strategy=self.abc.get("strategy", ""),
            commons_tribute="{0:.2f}".format(100 * self.abc.get("commonsTribute", "")),
            commons_tribute_remainder="{0:.2f}".format(100 - 100 * self.abc.get("commonsTribute", "")),
            entry_tribute="{0:.2f}".format(100 * self.abc.get("entryTribute", "")),
            exit_tribute="{0:.2f}".format(100 * self.abc.get("exitTribute", "")),
            reserve_ratio="{0:.2f}".format(100 * augmented_bonding_curve_output["chartData"]["reserveRatio"]),
            step=augmented_bonding_curve_output["stepTable"]["step"],
            current_price=augmented_bonding_curve_output["stepTable"]["currentPriceParsed"],
            amount_in=augmented_bonding_curve_output["stepTable"]["amountIn"],
            tribute_collected=augmented_bonding_curve_output["stepTable"]["tributeCollected"],
            amount_out=augmented_bonding_curve_output["stepTable"]["amountOut"],
            new_price=augmented_bonding_curve_output["stepTable"]["newPriceParsed"],
            price_slippage=augmented_bonding_curve_output["stepTable"]["slippage"],

            tao_voting_strategy=self.tao_voting.get("strategy", ""),
            support_required=self.tao_voting.get("supportRequired", ""),
            minimum_quorum=self.tao_voting.get("minimumQuorum", ""),
            vote_duration_days=self.tao_voting.get("voteDuration", ""),
            delegated_voting_days=self.tao_voting.get("delegatedVotingPeriod", ""),
            quiet_ending_days=self.tao_voting.get("quietEndingPeriod", ""),
            quiet_ending_extension_days=self.tao_voting.get("quietEndingExtension", ""),
            execution_delay_days=self.tao_voting.get("executionDelay", ""),
            vote_duration_days_1_extension = self.tao_voting.get("voteDuration", "") + self.tao_voting.get("executionDelay", ""),
            vote_duration_days_2_extensions = self.tao_voting.get("voteDuration", "") + self.tao_voting.get("quietEndingExtension", "") + self.tao_voting.get("executionDelay", ""),

            conviction_voting_strategy=self.conviction_voting.get("strategy", ""),
            conviction_growth_days=self.conviction_voting.get("convictionGrowth", ""),
            minimum_conviction=100 * self.conviction_voting.get("minimumConviction", ""),
            relative_spending_limit=100 * self.conviction_voting.get("spendingLimit", ""),
            effective_supply=conviction_voting_table["totalEffectiveSupply"],
            requested_amount=conviction_voting_table["requestedAmount"],
            amount_common_pool=conviction_voting_table["amountInCommonPool"],
            min_tokens_pass=conviction_voting_table["minTokensToPass"],
            tokens_pass_2_weeks=conviction_voting_table["tokensToPassIn2Weeks"],

            minimum_effective_supply=self.advanced_settings.get("minimumEffectiveSupply", ""),
            hatchers_rage_quit=self.advanced_settings.get("hatchersRageQuit", ""),
            virtual_balance="{:,}".format(self.advanced_settings.get("virtualBalance", ""))

        )
        return formated_output

    def generate_output(self):
        PARAMS_BOT_AUTH_TOKEN = os.getenv("PARAMS_BOT_AUTH_TOKEN")
        headers = {'Content-Type': 'application/json', 'Authorization': PARAMS_BOT_AUTH_TOKEN}
        data = {"title": self.title, "body": self.format_output_issue()}
        r = requests.post('https://api.github.com/repos/CommonsBuild/test-issues-config-dashboard/issues', data=json.dumps(data), headers=headers)
        return {"status": r.status_code, "url": r.json().get("html_url", "")}
