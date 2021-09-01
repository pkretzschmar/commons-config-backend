# Token Engineering Commons Upgrade Dashboard Backend

This repository contains the API for the four models of the Token Engineering Commons Upgrade Dashboard:
1. Token Freeze and Token Thaw
2. Augmented Bonding Curve (ABC)
3. Disputable Voting
4. Disputable Conviction Voting

## Models

### 1. Token Freeze and Token Thaw
The model inputs are:
- `OpeningPrice` (the initial price floor for the token)
- `TokenFreeze` (number of weeks that the opening price will be kept the same)
- `TokenThaw` (number of weeks in which the price floor will go from the opening price to zero)

The model output is a linechart data of the price floor over time and a table with the price floor and % of tokens unlocked in specific weeks.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/token-lockup/` with the following body:
```json
{
  "OpeningPrice": 5,
  "TokenFreeze": 20,
  "TokenThaw": 15
}
```

### 2. Augmented Bonding Curve
The model inputs are:
- `CommonsPercentage` (Percentage of funds that get substracted from the total funding to go to the commons pool. Between 0 and 95)
- `RagequitPercentage` (Percentage of supply burned before the bonding curve gets initialized. Between 0 and 20)
- `InitialPrice` (Initial token prive. No real limit but, expected to be between 1 and 4)
- `EntryTribute` (Percentage of funds substracted on buy (mint) operations before interacting with the bonding curve. Between 0 and 99)
- `ExitTribute` (Percentage of funds substracted on sell (burn) operations after interacting with the boding curve.  Between 0 and 99)
- `Steplist` Set of buy/sell operations applied to the bonding curve. AMOUNT IN THOUSANDS. List with format `[[AMOUNT, "TOKEN"],[AMOUNT, "TOKEN"]]`
- `ZoomGraph` optional, value 0 or 1. Used to specify if the draw function should show the whole curve(0) or "zoom in" into the area where operations are happening (1)

The model output is a linechart data of the price plotted over the wxDai balance and a table showing how price evolves when the steps are applied and the resulting tribute/slippage.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/augmented-bonding-curve/` with the following body:
```json
{ 
  "CommonsPercentage": 25,
  "RagequitPercentage": 5,
  "InitialPrice": 1.5,
  "EntryTribute": 5, 
  "ExitTribute": 5, 
  "HatchScenarioFunding": 1571.22357, 
  "Steplist": [[5, "TEC"], [1000, "wxDai"], [10, "TEC"]], 
  "ZoomGraph": 0
}
```

### 3. Disputable Voting
The model inputs are:
- `SupportRequired` (Minimum percentage of "yes" votes in relation to the total votes needed to a proposal pass)
- `MinimumQuorum` (Minimum percentage of quorum needed to a proposal pass)
- `VoteDuration` (Vote duration in days)
- `DelegatedVotingPeriod` (Delegated voting period in days)
- `QuietEndingPeriod` (Quiet ending period in days)
- `QuietEndingExtension` (Quiet ending extension in days)
- `ExecutionDelay` (Execution delay in days)

The model output is a bar chart plot of the voting timeline and a pie chart of the division of periods within the disputable voting.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/disputable-voting/` with the following body:
```json
{
  "SupportRequired": 0.4,
  "MinimumQuorum": 0.1,
  "VoteDuration": 7,
  "DelegatedVotingPeriod": 3,
  "QuietEndingPeriod": 2,
  "QuietEndingExtension": 1,
  "ExecutionDelay": 1
}
```

## Install

For setting up the Python3 virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

To install the requirements
```bash
pip install -r requirements.txt
```

## Usage

To run the development server locally
```bash
python main.py 
```
It can be reached at http://127.0.0.1:5000/.
