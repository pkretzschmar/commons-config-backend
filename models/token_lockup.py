import pandas as pd


class TokenLockupModel:
    def __init__(self,
                 opening_price=None,
                 token_freeze_period=None,
                 token_thaw_period=None):
        self.opening_price = opening_price if opening_price is not None else 100
        self.token_freeze_period = token_freeze_period if token_freeze_period is not None else 10
        self.token_thaw_period = token_thaw_period if token_thaw_period is not None else 30
        self.output_dict = {}
        self.output_dict['input'] = {
            'opening-price': self.opening_price,
            'token-freeze': self.token_freeze_period,
            'token-thaw': self.token_thaw_period
        }

    def get_data(self):
        weekly_token_thaw = self.opening_price / self.token_thaw_period
        df = pd.DataFrame({'week': range(1, 61)})
        df['price'] = 0
        df.loc[df['week'] <= self.token_freeze_period, 'price'] = self.opening_price
        df.loc[df['week'] > self.token_freeze_period, 'price'] = (self.opening_price - (df['week'] - self.token_freeze_period) * weekly_token_thaw)
        df.loc[df['price'] < 0, 'price'] = 0

        self.output_dict['output'] = df.to_dict(orient='list')

        return self.output_dict
