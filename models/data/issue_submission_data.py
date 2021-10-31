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
| Transferable            | {transferability}           |
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
![image](https://i.imgflip.com/5rop7m.jpg)

## What is the overall Commons Configuration strategy? 
{overall_strategy}

#### Advanced Settings Modified? {has_advanced_settings}

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

### Module 3: Tao Voting

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

| Duration                  | % of Tokens Released  | Price Floor of Token   |
| ------------------------- | --------------------- | ---------------------- |
| 3 months                  | {tokens_released[0]}% | {price_floor[0]} wxDAI |
| 6 months                  | {tokens_released[1]}% | {price_floor[1]} wxDAI |
| 9 months                  | {tokens_released[2]}% | {price_floor[2]} wxDAI |
| 1 year                    | {tokens_released[3]}% | {price_floor[3]} wxDAI |
| 1.5 years                 | {tokens_released[4]}% | {price_floor[4]} wxDAI |
| 2 years                   | {tokens_released[5]}% | {price_floor[5]} wxDAI |
| 3 years                   | {tokens_released[6]}% | {price_floor[6]} wxDAI |
| 4 years                   | {tokens_released[7]}% | {price_floor[7]} wxDAI |
| 5 years                   | {tokens_released[8]}% | {price_floor[8]} wxDAI |

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

|# of Quiet Ending Extensions                 | No Extensions                         | With 1 Extension                                  | With 2 Extensions                                  |
| ------------------------------------------- | ------------------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Time to Vote on Proposals**               | {vote_duration_days} days             | {vote_duration_days_1_extension} days             | {vote_duration_days_2_extensions} days             |
| **Time to Review a Delegates Vote**         | {review_duration_days} days           | {review_duration_days_1_extension} days           | {review_duration_days_2_extensions} days           |
| **Time to Execute a Passing Proposal**      | {execute_proposal_duration_days} days | {execute_proposal_duration_days_1_extension} days | {execute_proposal_duration_days_2_extensions} days |

- **Support Required**: **{support_required}%**, which means {support_required}% of all votes must be in favor of a proposal for it to pass.
- **Minimum Quorum**: **{minimum_quorum}%**, meaning that {minimum_quorum}% of all tokens need to have voted on a proposal in order for it to become valid.
- **Vote Duration**: **{vote_duration_days} day(s)**, meaning that eligible voters will have {vote_duration_days} day(s) to vote on a proposal. 
- **Delegated Voting Period** is set for **{delegated_voting_days} day(s)**, meaning that Delegates will have {delegated_voting_days} day(s) to use their delegated voting power to vote on a proposal. 
- **Quiet Ending Period**: **{quiet_ending_days} day(s)**, this means that {quiet_ending_days} day(s) before the end of the Vote Duration, if the vote outcome changes, the Quiet Ending Extension will be triggered. 
- **Quiet Ending Extension**: **{quiet_ending_extension_days} day(s)**, meaning that if the vote outcome changes during the Quiet Ending Period, an additional {quiet_ending_extension_days} day(s) will be added for voting.
- **Execution Delay**: **{execution_delay_days} days(s)**, meaning that there is an {execution_delay_days} day delay after the vote is passed before the proposed action is executed.  

### Strategy:
{tao_voting_strategy}

# Module 4: Conviction Voting

### Data: 
![](https://i.imgur.com/9RK5Hom.png)

| Proposal  | Requested Amount (wxDAI) | Common Pool (wxDAI)       | Effective supply (TEC)  | Tokens Needed To Pass (TEC) |
| --------- | ------------------------ | ------------------------- | ----------------------- | --------------------------- |
|     1     | {requested_amount[0]:,}  | {amount_common_pool[0]:,} | {effective_supply[0]:,} | {min_tokens_pass[0]}        |
|     2     | {requested_amount[1]:,}  | {amount_common_pool[1]:,} | {effective_supply[1]:,} | {min_tokens_pass[1]}        |
|     3     | {requested_amount[2]:,}  | {amount_common_pool[2]:,} | {effective_supply[2]:,} | {min_tokens_pass[2]}        |
|     4     | {requested_amount[3]:,}  | {amount_common_pool[3]:,} | {effective_supply[3]:,} | {min_tokens_pass[3]}        |
|     5     | {requested_amount[4]:,}  | {amount_common_pool[4]:,} | {effective_supply[4]:,} | {min_tokens_pass[4]}        |
|     6     | {requested_amount[5]:,}  | {amount_common_pool[5]:,} | {effective_supply[5]:,} | {min_tokens_pass[5]}        |

- **Conviction Growth**: **{conviction_growth_days} day(s)**, meaning that voting power will increase by 50% every {conviction_growth_days} days that they are staked behind a proposal, so after {double_conviction_growth_days} days, a voters voting power will have reached 75% of it's maximum capacity.
- **Minimum Conviction**: **{minimum_conviction}%**, this means that to pass any funding request it will take at least {minimum_conviction}% of the actively voting TEC tokens.
- The **Spending Limit**: **{relative_spending_limit}%**, which means that no more than {relative_spending_limit}% of the total funds in the Common Pool can be funded by a single proposal.

###  Strategy: 
{conviction_voting_strategy}

### [FORK THIS PROPOSAL](http://config.tecommons.org/config/import/{issue_number}) (link)

{advanced_settings_section}
"""
