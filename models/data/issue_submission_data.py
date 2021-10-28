advanced_settings_data = """
### *Advanced Settings 

>This will be empty or non-existent if the user did not change any advanced settings from their default. Any settings changed from default will show up here

| Parameter               | Value                       |
| ----------------------- | --------------------------- |
| Common Pool Amount      | {commons_pool_amount} wxDAI |
| HNY Liquidity           | {hny_liquidity} wxDAI       |
| Garden Liquidity        | {garden_liquidity} TEC      |
| Virtual Supply          | {virtual_supply} TEC        |
| Virtual Balance         | {virtual_balance} wxDAI     |
| Transferability         | {transferability}           |
| Token Name              | {token_name}                |
| Token Symbol            | {token_symbol}              |
| Proposal Deposit        | {proposal_deposit} wxDAI    |
| Challenge Deposit       | {challenge_deposit} wxDAI   |
| Settlement Period       | {settlement_period} days    |
| Minmum Effective Supply | {minimum_effective_supply}% |
| Hatchers Rage Quit      | {hatchers_rage_quit} wxDAI  |
| Initial Buy             | {initial_buy} wxDAI         |

[*Learn more about Advanced Settings on the TEC forum](https://forum.tecommons.org/c/defi-legos-and-how-they-work-together/adv-ccd-params/27)

### [FORK THIS PROPOSAL](http://config.tecommons.org/config/import/{issue_number}) (link)
"""

issue_data = """
#### Advanced Settings Modified? {has_advanced_settings}

## What is the overall Commons Configuration strategy? 
{overall_strategy}

### [FORK THIS PROPOSAL](http://config.tecommons.org/config/import/{issue_number}) (link)

# Summary 
### Module 1: Token Freeze & Token Thaw

| Parameter     | Value                       |
| ------------- | --------------------------- |
| Token Freeze  | {token_freeze_period} Weeks |
| Token Thaw    | {token_thaw_period} Weeks   |
| Opening Price | {opening_price} wxDAI       |

### Module 2: Augmented Bonding Curve 

| Parameter        | Value              |
| ---------------- | ------------------ |
| Commons Tribute  | {commons_tribute}% |
| Entry Tribute    | {entry_tribute}%   |
| Exit Tribute     | {exit_tribute}% |
| *_Reserve Ratio_ | {reserve_ratio}%   |

*This is an output. [Learn more about the Reserve Ratio here](https://forum.tecommons.org/t/augmented-bonding-curve-opening-price-reserve-ratio/516).

### Module 3: Disputable Voting

| Parameters              | Value                                |
| ----------------------- | ------------------------------------ |
| Support Required        | {support_required}%                  |
| Minimum Quorum          | {minimum_quorum}%                    |
| Vote Duration           | {vote_duration_days} days(s)         |
| Delegated Voting Period | {delegated_voting_days} day(s)       |
| Quiet Ending Period     | {quiet_ending_days} day(s)           |
| Quiet Ending Extension  | {quiet_ending_extension_days} day(s) |
| Execution Delay         | {execution_delay_days} day(s)       |


### Module 4: Conviction Voting

| Parameter          | Value                           |
| ------------------ | ------------------------------- |
| Conviction Growth  | {conviction_growth_days} day(s) |
| Minimum Conviction | {minimum_conviction}%           |
| Spending Limit     | {relative_spending_limit}%      |

# Module 1: Token Freeze and Token Thaw

### Data:
![](https://i.imgur.com/Wk3jgGo.jpg)

| # of Weeks                   | % of Tokens Released  | Price Floor of Token   |
| ---------------------------- | --------------------- | ---------------------- |
| {token_lockup_week[0]} weeks | {tokens_released[0]}% | {price_floor[0]} wxDAI |
| {token_lockup_week[1]} weeks | {tokens_released[1]}% | {price_floor[1]} wxDAI |
| {token_lockup_week[2]} weeks | {tokens_released[2]}% | {price_floor[2]} wxDAI |
| {token_lockup_week[3]} weeks | {tokens_released[3]}% | {price_floor[3]} wxDAI |
| {token_lockup_week[4]} weeks | {tokens_released[4]}% | {price_floor[4]} wxDAI |
| {token_lockup_week[5]} weeks | {tokens_released[5]}% | {price_floor[5]} wxDAI |

- **Token Freeze**: **{token_freeze_period} weeks**, meaning that 100% of TEC tokens minted for Hatchers will remain locked from being sold or transferred for {token_freeze_period} weeks. They can still be used to vote while frozen.
- **Token Thaw**: **{token_thaw_period} weeks**, meaning the Hatchers frozen tokens will start to become transferable at a steady rate starting at the end of Token Freeze and ending {token_thaw_period} weeks later.
- **Opening Price**: **{opening_price} wxDAI**, meaning for the initial buy, the first TEC minted by the Augmented Bonding Curve will be priced at {opening_price} wxDAI making it the price floor during the Token Freeze. 

### Strategy:
{token_lockup_strategy}

# Module 2: Augmented Bonding Curve (ABC)

### Data:

![](https://i.imgur.com/44MoI7N.png)

| Step #             | Current Price      | Amount In      | Tribute Collected      | Amount Out      | New Price      | Price Slippage      |
| ------------------ | ------------------ | -------------- | ---------------------- | --------------- | -------------- | ------------------- |
{abc_steps}

#### NOTE: 
We're very bullish on TEC so we provide the BUY scenario at launch to compare proposals... to explore this proposal's ABC further Click the link  below to see their parameters in your dashboard, be warned this will clear any data you have in your dashboard: 

### [FORK THIS PROPOSAL](http://config.tecommons.org/config/import/{issue_number}) (link)

| Allocation of Funds              | wxDAI                    |
|----------------------------------|--------------------------|
| Common Pool (Before Initial Buy) | {common_pool_before}     |
| Reserve (Before Initial Buy)     | {reserve_balance_before} |
| Common Pool (After Initial Buy)  | {common_pool_after}      |
| Reserve (After Initial Buy)      | {reserve_balance_after}  |

- **Commons Tribute**: **{commons_tribute}%**, which means that {commons_tribute}% of the Hatch funds ({common_pool_before} wxDAI)  will go to the Common Pool and {commons_tribute_remainder}% ({reserve_balance_before} wxDAI) will go to the ABC's Reserve.
- **Entry Tribute**: **{entry_tribute}%** meaning that from every **BUY** order on the ABC, {entry_tribute}% of the order value in wxDAI is subtracted and sent to the Common Pool.
- **Exit Tribute**: **{exit_tribute}%** meaning that from every **SELL** order on the ABC, {exit_tribute}% of the order value in wxDAI is subtracted and sent to the Common Pool. 

### Strategy:
{abc_strategy}

# Module 3: Tao Voting

### Data: 

![](https://i.imgur.com/9RK5Hom.png)

|# of Quiet Ending Extensions                 | No Extensions             | With 1 Extension                      | With 2 Extensions                      |
| ------------------------------------------- | ------------------------- | ------------------------------------- | -------------------------------------- |
| **Total Amount of Time to Complete a Vote** | {vote_duration_days} days | {vote_duration_days_1_extension} days | {vote_duration_days_2_extensions} days |

- **Support Required**: **{support_required}%**, which means {support_required}% of all votes must be in favor of a proposal for it to pass.
- **Minimum Quorum**: **{minimum_quorum}%**, meaning that {minimum_quorum}% of all tokens need to have voted on a proposal in order for it to become valid.
- **Vote Duration**: **{vote_duration_days} day(s)**, meaning that eligible voters will have {vote_duration_days} day(s) to vote on a proposal. 
- **Delegated Voting Period** is set for **{delegated_voting_days} day(s)**, meaning that Delegates will have {delegated_voting_days} day(s) to use their delegated voting power to vote on a proposal. 
- **Quiet Ending Period**: **{quiet_ending_days} day(s)**, this means that {quiet_ending_days} day(s) before the end of the Vote Duration, if the vote outcome changes, the Quiet Ending Extension will be triggered. 
- **Quiet Ending Extension**: **{quiet_ending_extension_days} day(s)**, meaning that if the vote outcome changes during the Quiet Ending Period, an additional {quiet_ending_extension_days} day(s) will be added for voting.
- **Execution Delay**: **{execution_delay_days} days(s)**, meaning that there is an {execution_delay_days} day delay after the vote is passed before the proposed action is executed.  

### Strategy:
{tao_voting_strategy}

# Module 4: Conviction Voting Strategy

### Data: 
![](https://i.imgur.com/9RK5Hom.png)

| Variables                        | Scenario 1                | Scenario 2                | Scenario 3                | Scenario 4                | Scenario 5                | Scenario 6                |
| -------------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| **Effective Supply**             | {effective_supply[0]}     | {effective_supply[1]}     | {effective_supply[2]}     | {effective_supply[3]}     | {effective_supply[4]}     | {effective_supply[5]}     |
| **Requested Amount (wxDAI)**     | **{requested_amount[0]}** | **{requested_amount[1]}** | **{requested_amount[2]}** | **{requested_amount[3]}** | **{requested_amount[4]}** | **{requested_amount[5]}** |
| Amount in Common Pool (wxDAI)    | {amount_common_pool[0]}   | {amount_common_pool[1]}   | {amount_common_pool[2]}   | {amount_common_pool[3]}   | {amount_common_pool[4]}   | {amount_common_pool[5]}   |
| Minimum Tokens Needed to Pass    | {min_tokens_pass[0]}      | {min_tokens_pass[1]}      | {min_tokens_pass[2]}      | {min_tokens_pass[3]}      | {min_tokens_pass[4]}      | {min_tokens_pass[5]}      |
| Tokens Needed To Pass in 2 weeks | {tokens_pass_2_weeks[0]}  | {tokens_pass_2_weeks[1]}  | {tokens_pass_2_weeks[2]}  | {tokens_pass_2_weeks[3]}  | {tokens_pass_2_weeks[4]}  | {tokens_pass_2_weeks[5]}  |

- **Conviction Growth**: **{conviction_growth_days} day(s)**, meaning that voting power will increase by 50% every {conviction_growth_days} days that they are staked behind a proposal, so after {double_conviction_growth_days} days, a voters voting power will have reached 75% of it's maximum capacity.
- **Minimum Conviction**: **{minimum_conviction}%**, this means that to pass any funding request it will take at least {minimum_conviction}% of the actively voting TEC tokens.
- The **Spending Limit**: **{relative_spending_limit}%**, which means that no more than {relative_spending_limit}% of the total funds in the Common Pool can be funded by a single proposal.

###  Strategy: 
{conviction_voting_strategy}

| Variables                        | Scenario 1                | Scenario 2                | Scenario 3                | Scenario 4                | Scenario 5                | Scenario 6                |
| -------------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| **Effective Supply**             | {effective_supply[0]}     | {effective_supply[1]}     | {effective_supply[2]}     | {effective_supply[3]}     | {effective_supply[4]}     | {effective_supply[5]}     |
| **Requested Amount (wxDAI)**     | **{requested_amount[0]}** | **{requested_amount[1]}** | **{requested_amount[2]}** | **{requested_amount[3]}** | **{requested_amount[4]}** | **{requested_amount[5]}** |
| Amount in Common Pool (wxDAI)    | {amount_common_pool[0]}   | {amount_common_pool[1]}   | {amount_common_pool[2]}   | {amount_common_pool[3]}   | {amount_common_pool[4]}   | {amount_common_pool[5]}   |
| Minimum Tokens Needed to Pass    | {min_tokens_pass[0]}      | {min_tokens_pass[1]}      | {min_tokens_pass[2]}      | {min_tokens_pass[3]}      | {min_tokens_pass[4]}      | {min_tokens_pass[5]}      |
| Tokens Needed To Pass in 2 weeks | {tokens_pass_2_weeks[0]}  | {tokens_pass_2_weeks[1]}  | {tokens_pass_2_weeks[2]}  | {tokens_pass_2_weeks[3]}  | {tokens_pass_2_weeks[4]}  | {tokens_pass_2_weeks[5]}  |


### [FORK THIS PROPOSAL](http://config.tecommons.org/config/import/{issue_number}) (link)

{advanced_settings_section}
"""
