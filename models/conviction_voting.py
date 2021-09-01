import pandas as pd
import numpy as np

class ConvictionVotingModel:
    def __init__(self,
                 spending_limit=None,
                 minimum_conviction=None,
                 conviction_growth=None):
        self.spending_limit = spending_limit if spending_limit is not None else 0.2
        self.minimum_conviction = minimum_conviction if minimum_conviction is not None else 0.05
        self.conviction_growth = conviction_growth if conviction_growth is not None else 2
        self.staked_on_proposal = 1
        self.staked_on_other_proposals = 0
        self.min_active_stake_pct = 0.05
        self.output_dict = {}
        self.output_dict['input'] = {
            'spendingLimit': self.spending_limit,
            'minimumConviction': self.minimum_conviction,
            'convictionGrowth': self.conviction_growth,
        }
    
    def get_decay(self):
        return (1 / 2) ** (1 / self.conviction_growth)
    
    def get_conviction(self, initial_conviction, amount, time):
        return initial_conviction * self.get_decay() ** time + (amount * (1 - self.get_decay() ** time)) / (1 - self.get_decay())

    def get_max_conviction(self, amount):
        return amount / (1 - self.get_decay())
    
    def get_staked_on_proposals(self):
        return self.staked_on_proposal + self.staked_on_other_proposals

    def get_staked(self, staked = None):
        if staked is None:
            staked = self.get_staked_on_proposals()
        return np.where(staked > self.min_active_stake_pct, staked, self.min_active_stake_pct)


    def get_data(self):
        # Conviction Growth Chart Data
        x = np.linspace(0, 5 * self.conviction_growth,100)
        y = 100 * self.get_conviction(0, self.staked_on_proposal, time=x) / self.get_max_conviction(self.get_staked())
        df_growth = pd.DataFrame(zip(x, y), columns=['timeDays','convictionPercentage'])
        
        x2 = np.linspace(5 * self.conviction_growth,10 * self.conviction_growth,1000)
        y2 = y[-1] * self.get_decay()**x
        df_decay = pd.DataFrame(zip(x2, y2), columns=['timeDays','convictionPercentage'])
        
        df = pd.concat([df_growth, df_decay])
        self.output_dict['output'] = {'convictionGrowthChart' : df.to_dict(orient='list')}
        self.output_dict['output']['maxConvictionGrowthXY'] = {
            'x': df_growth.iloc[df_growth['convictionPercentage'].idxmax()]['timeDays'],
            'y': df_growth.iloc[df_growth['convictionPercentage'].idxmax()]['convictionPercentage'],
        }

        self.output_dict['output']['convictionGrowth80PercentageXY'] = {
            'x': df_growth.iloc[df_growth[df_growth.convictionPercentage >= 80].first_valid_index()]['timeDays'],
            'y': df_growth.iloc[df_growth[df_growth.convictionPercentage >= 80].first_valid_index()]['convictionPercentage'],
        }

        return self.output_dict
