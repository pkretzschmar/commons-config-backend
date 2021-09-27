test_issue_data = """
# My Submission Title

#### Advanced Settings Modified? (Yes or No)

## What is your overall Commons Configuration strategy? 
The proposer here should outline their big picture thought process for the settings they chose. Also here they can highlight if their proposal is a fork, what they changed or perhaps any unique and/or contentious settings they chose and why.

### [FORK MY PROPOSAL]() (link)

# Module 1: Token Freeze and Token Thaw 
- **Token Freeze** is set to **{token_freeze_period} weeks**, meaning that 100% of TEC tokens minted for Hatchers will remain locked from being sold or transferred for {token_freeze_period} weeks. 
- **Token Thaw** is set to **{token_thaw_period} weeks**, meaning that from the end of Token Freeze, over the course of {token_thaw_period} weeks tokens minted for Hatchers gradually become liquid. At the end of {token_thaw_period} weeks 100% of the Hatchers' TEC tokens have become liquid.
- The **Opening Price** is set to **{opening_price} wxDAI**, meaning at the outset of the Commons Upgrade the price to buy TEC on the Augmented Bonding Curve will be {opening_price} wxDAI. 

### Strategy:
Here the proposer can explain their parameter choices, briefly or in depth if they choose.

### Data:
![](https://i.imgur.com/Wk3jgGo.jpg)


| # of Weeks | % of Tokens Released | Price Floor of Token |
| ---------- | -------------------- | -------------------- |
| 5 weeks    | 0%                   | 2 wxDAI              |
| 10 weeks   | 0%                   | 2 wxDAI              |
| 20 weeks   | 40%                  | 1.10 wxDAI           |
| 30 weeks   | 60%                  | 0.80 wxDAI           |
| 40 weeks   | 80%                  | 0.45 wxDAI           |
| 52 weeks   | 100%                 | 0.00 wxDAI           |



# Module 2: Augmented Bonding Curve (ABC)
- **Commons Tribute** is set to **{commons_tribute}%**, which means that {commons_tribute}% of the Hatch funds will go to the Common Pool and {commons_tribute_remainder}% will go to the Reserve Balance.
- **Entry Tribute** is set to **{entry_tribute}%** meaning that from every **BUY** order on the ABC, {entry_tribute}% of the order value in wxDAI is subtracted and sent to the Common Pool.
- **Exit Tribute** is set to **{exit_tribute}%** meaning that from every **SELL** order on the ABC, {exit_tribute}% of the order value in wxDAI is subtracted and sent to the Common Pool. 

### Strategy:
Here the proposer can explain their parameter choices, briefly or in depth if they choose.

### Data:

>We're very bullish on TEC so we only provide the BUY scenario as the standard 3 steps that are used to compare different proposals

![](https://i.imgur.com/44MoI7N.png)

<table>
<tr>
<td>Step #
</td>
<td>Current Price
<p>
<em>wxDAI/TEC</em>
</td>
<td>Amount In
</td>
<td>Tribute Collected 
(wxDAI)
</td>
<td>Amount Out
</td>
<td>New Price
<p>
<em>wxDAI/TEC</em>
</td>
<td>Price Slippage
</td>
</tr>
<tr>
<td><strong>Step 1</strong>
</td>
<td>2.00
</td>
<td>200 wxDAI
</td>
<td>10.00
</td>
<td>80 TEC
</td>
<td>2.83
</td>
<td>6.2%
</td>
</tr>
<tr>
<td><strong>Step 2</strong>
</td>
<td>2.83
</td>
<td>2000 wxDAI
</td>
<td>100
</td>
<td>704 TEC
</td>
<td>5.776 
</td>
<td>104%
</td>
</tr>
<tr>
<td><strong>Step 3</strong>
</td>
<td>5.776
</td>
<td>60 TEC
</td>
<td>67.43
</td>
<td>263.48 wxDAI
</td>
<td>5.42
</td>
<td>6.2%
</td>
</tr>
</table>



# Module 3: Tao Voting 
- **Support Required** is set to **{support_required}%**, which means {support_required}% of all votes must be in favour of a proposal for it to pass.
- **Minimum Quorum** is set to **{minimum_quorum}%**, meaning that {minimum_quorum}% of all tokens need to have voted on a proposal in order for it to become valid.
- **Vote Duration** is **{vote_duration_days} day(s)**, meaning that eligible voters will have {vote_duration_days} day(s) to vote on a proposal. 
- **Delegated Voting Period** is set for **{delegated_voting_days} day(s)**, meaning that Delegates will have {delegated_voting_days} day(s) to use their delegated voting power to vote on a proposal. 
- **Quiet Ending Period** is set to **{quiet_ending_days} day(s)**, this means that {quiet_ending_days} day(s) before the end of the Vote Duration, if the vote outcome changes, the Quiet Ending Extension will be triggered. 
- **Quiet Ending Extension** is set to **{quiet_ending_extension_days} day(s)**, meaning that if the vote outcome changes during the Quiet Ending Period, an additional {quiet_ending_extension_days} day(s) will be added for voting.
- **Execution Delay** is set to **{execution_delay_hours} hour(s)**, meaning that there is an {execution_delay_hours} hour delay after the vote is passed before the proposed action is executed.  
### Strategy:
Here the proposer can explain their parameter choices, briefly or in depth if they choose.

### Data: 


![](https://i.imgur.com/UE0J1sR.png)



|# of Quiet Ending Extensions  | No Extensions | With 1 Extension | With 2 Extensions |
| --------------------------------------- | ------------- | ---------------- | ----------------- |
| **Total Amount of Time to Complete a Vote**                   | 5 days        | 7 days           | 9 days            |



# Module 4: Conviction Voting Strategy
- **Conviction Growth** is set to **{conviction_growth_days} day(s)**, meaning that Conviction will increase by 50% every {conviction_growth_days} day(s).
- **Minimum Conviction** is set to **{minimum_conviction}%**, this means that to pass a funding request for an infinitely small amount will still take a minimum of {minimum_conviction}% of the total TEC currently active in the Conviction Voting application.
- The **Spending Limit** is set to **{relative_spending_limit}%**, which means that no more than {relative_spending_limit}% of the total funds in the Common Pool can be requested by single proposal. 
###  Strategy: 
Here the proposer can explain their parameter choices, briefly or in depth if they choose.


### Data: 
![](https://i.imgur.com/9RK5Hom.png)



| Variables                        | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 | Scenario 5   | Scenario 6   |
| -------------------------------- | ---------- | ---------- | ---------- | ---------- | ------------ | ------------ |
| **Effective Supply**               |  1,000,000          |1,000,000            |  1,000,000          |1,000,000            |1,000,000              |1,000,000              |
| **Requested Amount (wxDAI)**     | **1,000**  | **1,000**  | **5,000**  | **5,000**  | **25,000**   | **25,000**   |
| Amount in Common Pool (wxDAI)    | 100,000    | 750,000    | 100,000    | 750,000    | 100,000      | 750,000      |
| Minimum Tokens Needed to Pass    | 12,000     | 10,000     | 20,000     | 15,000     | Not possible | 150,000      |
| Tokens Needed To Pass in 2 weeks | 25,000     | 20,000     | 50,000     | 40,000     | Not possible | Not possible |
------

### [FORK MY PROPOSAL]() (link)


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
| Exit Tribute     | {commons_tribute}% |
| *_Reserve Ratio_ | 20%                |

*Reserve Ratio is an output derived from the Opening Price and Commons Tribute. [Learn more about the Reserve Ratio here](https://forum.tecommons.org/t/augmented-bonding-curve-opening-price-reserve-ratio/516).

### Module 3: Disputable Voting

| Parameters              | Value                                |
| ----------------------- | ------------------------------------ |
| Support Required        | {support_required}%                  |
| Minimum Quorum          | {minimum_quorum}%                    |
| Vote Duration           | {vote_duration_days} days(s)         |
| Delegated Voting Period | {delegated_voting_days} day(s)       |
| Quiet Ending Period     | {quiet_ending_days} day(s)           |
| Quiet Ending Extension  | {quiet_ending_extension_days} day(s) |
| Execution Delay         | {execution_delay_hours} hour(s)      |


### Module 4: Conviction Voting

| Parameter          | Value                           |
| ------------------ | ------------------------------- |
| Conviction Growth  | {conviction_growth_days} day(s) |
| Minimum Conviction | {minimum_conviction}%           |
| Spending Limit     | {relative_spending_limit}%      |

### *Advanced Settings 

>This will be empty or non-existant if the user did not change any advanced settings from their default. Any settings changed from default will show up here

| Parameter               | Value                       |
| ----------------------- | --------------------------- |
| Minmum Effective Supply | {minimum_effective_supply}% |
| Hatchers Rage Quit      | {hatchers_rage_quit}%       |
| Virtual Balance         | {virtual_balance} wxDAI     |

[*Learn more about Advanced Settings on the TEC forum](https://forum.tecommons.org/c/defi-legos-and-how-they-work-together/adv-ccd-params/27)

### [FORK MY PROPOSAL]() (link)
"""
