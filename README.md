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

The model output is a linechart data of the price floor over time.

To do an API call with the model input and receive the model outputs, it uses a POST request through the route `/token-lockup/` with the following body:
```json
{
  "opening-price": 5,
  "token-freeze": 20,
  "token-thaw": 15
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
