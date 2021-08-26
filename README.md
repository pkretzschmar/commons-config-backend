# Token Engineering Commons Upgrade Dashboard Backend

This repository contains the API for the four models of the Token Engineering Commons Upgrade Dashboard:
1. Token Freeze and Token Thaw
2. Augmented Bonding Curve (ABC)
3. Disputable Voting
4. Disputable Conviction Voting

## Models

### 1. Token Freeze and Token Thaw
The model inputs are:
- `opening-price` (the initial price floor for the token)
- `token-freeze` (number of weeks that the opening price will be kept the same)
- `token-thaw` (number of weeks in which the price floor will go from the opening price to zero)

The model output is a linechart data of the price floor over time and a table with the price floor and % of tokens unlocked in specific weeks.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/token-lockup/` with the following body:
```json
{
  "opening-price": 5,
  "token-freeze": 20,
  "token-thaw": 15
}
```

### 2. Augmented Bonding Curve
The model inputs are:
- `commons_percentage` (Percentage of funds that get substracted from the total funding to go to the commons pool. Between 0 and 95)
- `ragequit_percentage` (Percentage of supply burned before the bonding curve gets initialized. Between 0 and 20)
- `initial_price` (Initial token prive. No real limit but, expected to be between 1 and 4)
- `entry_tribute` (Percentage of funds substracted on buy (mint) operations before interacting with the bonding curve. Between 0 and 99)
- `exit_tribute` (Percentage of funds substracted on sell (burn) operations after interacting with the boding curve.  Between 0 and 99)
- `steplist` Set of buy/sell operations applied to the bonding curve. AMOUNT IN THOUSANDS. List with format `[[AMOUNT, "TOKEN"],[AMOUNT, "TOKEN"]]`
- `zoom_graph` optional, value 0 or 1. Used to specify if the draw function should show the whole curve(0) or "zoom in" into the area where operations are happening (1)

The model output is a linechart data of the price plotted over the wxDai balance and a table showing how price evolves when the steps are applied and the resulting tribute/slippage.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/augmented-bonding-curve/` with the following body:
```json
{ 
  "commons-percentage": 25,
  "ragequit-percentage": 5,
  "initial-price": 1.5,
  "entry-tribute": 5, 
  "exit-tribute": 5, 
  "hatch-scenario-funding": 1571.22357, 
  "steplist": [[5, "TEC"], [1000, "wxDai"], [10, "TEC"]], 
  "zoom-graph": 0
}
```

### 3. Disputable Voting
The model inputs are:
- `support-required` (Minimum percentage of "yes" votes in relation to the total votes needed to a proposal pass)
- `minimum-quorum` (Minimum percentage of quorum needed to a proposal pass)
- `vote-duration` (Vote duration in days)
- `delegated-voting-period` (Delegated voting period in days)
- `quiet-ending-period` (Quiet ending period in days)
- `quiet-ending-extension` (Quiet ending extension in days)
- `execution-delay` (Execution delay in days)

The model output is a bar chart plot of the voting timeline and a pie chart of the division of periods within the disputable voting.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/disputable-voting/` with the following body:
```json
{
  "support-required": 0.4,
	"minimum-quorum": 0.1,
	"vote-duration": 7,
	"delegated-voting-period": 3,
	"quiet-ending-period": 2,
	"quiet-ending-extension": 1,
	"execution-delay": 1
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
