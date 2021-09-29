import os
import pandas as pd
import numpy as np


#These numbers are fixed from the hatch results (in thousands)
TOTAL_HATCH_FUNDING = 1571.22357 
TOTAL_INITIAL_TECH_SUPPLY= 2035.918945 


class BondingCurveInitializer:

    def __init__(self, reserve_balance=100, opening_price=5, initial_supply=100):
        self.opening_price = opening_price
        self.initial_supply = initial_supply
        self.initial_balance = reserve_balance

    def reserve_ratio(self):
        return self.initial_balance / (self.opening_price * self.initial_supply)
    
    #Returns the token price given a specific supply
    def get_price(self, supply):
        return (supply ** ((1 / self.reserve_ratio()) - 1) * self.opening_price) / (
            self.initial_supply ** ((1 / self.reserve_ratio()) - 1)
        )

    #Returns the collateral balance price given a specific supply
    def get_balance(self, supply):
        return (
            self.reserve_ratio() * self.get_price(supply) * supply
        )

    #Returns supply at a specific balance. THIS IS AN APPROXIMATION only meant for visualizing scenarios
    def get_supply(self, balance):
        supply_ref = 0
        while self.get_balance(supply_ref) <  balance:
            supply_ref = supply_ref + 10

        df = self.curve_over_balance(supply_ref-10, supply_ref, 100000)
        df_rounded = df.round(3)
        
        index= int(df.index.where(df_rounded['balanceInThousands'] >= balance).dropna()[0])
        price = df.at[index, "price"]

        supply = balance/(price* self.reserve_ratio())
        

        return supply

    #For drawing the bonding curve. Range shows how many times the initial supply you make the graph for, steps how many subdivisions
    def curve_over_supply(self, range_begin=0, range_end=1000, steps=500):
        x = np.linspace(range_begin, range_end, steps)
        y = self.get_price(x)

        return pd.DataFrame(zip(x, y), columns=["supplyInThousands", "price"])
    
    def curve_over_balance(self, range_begin=0, range_end=1000, steps=500):
        supply_list = np.linspace(range_begin, range_end, steps)
        x = self.get_balance(supply_list)
        y = self.get_price(supply_list)

        return pd.DataFrame(zip(x, y), columns=["balanceInThousands", "price"])



class BondingCurve(BondingCurveInitializer):

    def __init__(self, reserve_balance=100, opening_price=5, initial_supply=100, entry_tribute=0.05, exit_tribute=0.05):
        super().__init__(reserve_balance, opening_price, initial_supply)
        self.current_supply = self.initial_supply
        self.current_balance = self.get_balance(self.initial_supply)
        self.entry_tribute = entry_tribute
        self.exit_tribute = exit_tribute

    def set_new_supply(self, new_supply):
        self.current_supply = new_supply
        self.current_balance = self.get_balance(new_supply)

    #Returns how much wxDAI you get from selling TEC. Informative, doesn't change state
    def sale_return(self, bonded):
        return self.current_balance * (
            (bonded / self.current_supply + 1) ** (1 / self.reserve_ratio()) - 1
        )

    #Returns how much TEC you get from purchasing with wxDAI. Informative, doesn't change state
    def purchase_return(self, collateral):
        return self.current_supply * (
            (collateral / self.current_balance + 1) ** (self.reserve_ratio()) - 1
        )



class BondingCurveHandler():
    '''
    The handler for the Bonding Curve. All interaction happens through this.

    The constrctor receives following args:

    commons_percentage: float between 0-0.95. Percentage of funds that get substracted from the total funding to go to the commons pool
    ragequit_percentage: int between 0-0.20. Percentage of supply burned before the bonding curve gets initialized
    opening_price: float. No real limit but, expected to be between 1 and 4
    entry_tribute: float between 0-0.99. Percentage of funds substracted on buy (mint) operations before interacting with the bonding curve
    exit_tribute: float between 0-0.99. Percentage of funds substracted on sell (burn) operations after interacting with the boding curve
    steplist: list with format [["AMOUNT", "TOKEN"],["AMOUNT", "TOKEN"]]. Set of buy/sell operations applied to the bonding curve.
    zoom_graph=0: optional. value 0 or 1. To specify if the draw function should show the whole curve(0) or "zoom in" into the area where operations are happening (1)
    plot_mode=0: optional. value 0 or 1. Not in the scope of this iteration. Specifies if the draw function should plot the price against the balance (0) or the supply (1)
    
    '''

    def __init__(self,
                 commons_percentage,
                 ragequit_percentage,
                 opening_price,
                 entry_tribute,
                 exit_tribute,
                 scenario_reserve_balance,
                 steplist,
                 zoom_graph=0,
                 plot_mode=0):
        #
        #check here for validity of parameters
        #
        params_valid = self.check_param_validity( 
                 commons_percentage,
                 ragequit_percentage,
                 opening_price,
                 entry_tribute,
                 exit_tribute,
                 float(scenario_reserve_balance),
                 steplist,
                 int(zoom_graph),
                 int(plot_mode)
                 )
        #The numbers for initial supply and taken from the constants
        self.bonding_curve = self.create_bonding_curve(commons_percentage=commons_percentage, ragequit_percentage=ragequit_percentage, opening_price=opening_price, entry_tribute= entry_tribute / 100, exit_tribute= exit_tribute / 100)
        
        #set the current supply to the point where the scenarios are going to happen
        if(float(scenario_reserve_balance) != TOTAL_HATCH_FUNDING):
            scenario_supply= self.bonding_curve.get_supply(float(scenario_reserve_balance))
            self.bonding_curve.set_new_supply(scenario_supply)
        
        self.steps_table = self.generate_outputs_table(bondingCurve= self.bonding_curve, steplist= steplist)
        self.zoom_graph = zoom_graph
        self.plot_mode = plot_mode
    

    def get_data(self):

        [min_range, max_range] = self.get_scenario_range(steps_table= self.steps_table, zoom_graph=self.zoom_graph)

        clean_figure_data = self.get_data_augmented_bonding_curve(bondingCurve= self.bonding_curve, min_range=min_range, max_range=max_range, plot_mode=self.plot_mode).to_dict(orient='list')
        clean_figure_data['reserveRatio'] = self.bonding_curve.reserve_ratio()
        
        figure_bonding_curve= {"chartData": {}}
        figure_milestone_table =self.get_milestone_table(self.bonding_curve) 
        
        #reserve_ratio = {"reserveRatio": self.bonding_curve.reserve_ratio()}

        if self.steps_table.empty:
            figure_bonding_curve['chartData'] = clean_figure_data
            figure_bonding_curve['milestoneTable'] = figure_milestone_table
            return figure_bonding_curve
        else: 
            figure_buy_sell_table =self.steps_table.loc[:,["step", "currentPriceParsed", "amountIn", "tributeCollected", "amountOut", "newPriceParsed", "slippage"]].to_dict(orient='list')
            extended_figure_data = clean_figure_data
            #get single points with full coordinates
            extended_figure_data['singlePoints'] = self.get_single_point_coordinates(self.steps_table)
            #get linspace from every step.
            extended_figure_data['stepLinSpaces'] = self.get_step_linspaces(self.bonding_curve, self.steps_table)

            figure_bonding_curve['chartData'] = extended_figure_data
            figure_bonding_curve['stepTable'] = figure_buy_sell_table
            figure_bonding_curve['milestoneTable'] = figure_milestone_table

            return figure_bonding_curve

    def create_bonding_curve(self, commons_percentage=0.5, ragequit_percentage=0.05,  opening_price=3, entry_tribute=0.05, exit_tribute=0.05):
        
        initial_supply = TOTAL_INITIAL_TECH_SUPPLY * (1 - ragequit_percentage)
        hatch_funding= TOTAL_HATCH_FUNDING * (1 - ragequit_percentage)

        initial_reserve = hatch_funding - (hatch_funding * commons_percentage)
        
        bCurve = BondingCurve(initial_reserve, opening_price, initial_supply, entry_tribute, exit_tribute)

        return bCurve

    def generate_outputs_table(self, bondingCurve, steplist):

        column_names = [
            "step",
            "currentPrice",
            "currentPriceParsed",
            "currentSupply",
            "currentBalance",
            "amountIn",
            "tributeCollected",
            "amountOut",
            "newPrice",
            "newPriceParsed",
            "newSupply",
            "newBalance",
            "slippage",
        ]
        outputTable = pd.DataFrame(columns=column_names)

        for index, step in enumerate(steplist):

            current_price = bondingCurve.get_price(bondingCurve.current_supply)
            current_price_parsed = str(format(current_price, '.2f')) + " wxDAI"
            #current_price_parsed = str(round(current_price, 2)) + " wxDAI"

            amount_in = step[0]
            token_type = "wxDAI" if step[1] == "wxDai" else step[1] #to avoid the most obvious error. TO DO: in-depth validation of the steplist...
            
            amount_in_parsed = str(format(amount_in, '.2f')) + "k " + str(token_type)
            #amount_in_parsed = str(round(amount_in, 2)) + "k " + str(token_type)
        
            amount_out = 0
            amount_out_parsed = ""
            new_supply = 0
            tribute_collected = 0
            if token_type == "wxDAI":
                # take tribute and buy
                tribute_collected = amount_in * bondingCurve.entry_tribute
                amountAfterTribute = amount_in - tribute_collected

                amount_out = bondingCurve.purchase_return(amountAfterTribute)
                amount_out_parsed = str(format(amount_out, '.2f')) + "k TEC"
                #amount_out_parsed = str(round(amount_out, 2)) + "k TEC"
                tribute_collected_parsed = str(format(tribute_collected, '.2f')) + "k wxDAI"
                #tribute_collected_parsed = str(round(tribute_collected, 2)) + "k wxDAI"

                slippage = (amount_in - tribute_collected)/bondingCurve.get_price(bondingCurve.current_supply) - amount_out
                slippage_pct = slippage / ((amount_in - tribute_collected)/bondingCurve.get_price(bondingCurve.current_supply))
                slippage_pct = str(format((slippage_pct*100), '.2f')) + "%"

                new_supply = max(
                    0, bondingCurve.current_supply + amount_out
                )
            elif token_type == "TEC":
                #this section works, but all the -1 mults are a bit of a mess. 
                # sell and take tribute
                amount_in = amount_in * -1 #because we are reducing the supply (burning)
                amountBeforeTribute = bondingCurve.sale_return(amount_in)            

                tribute_collected = amountBeforeTribute * bondingCurve.exit_tribute #since it is a sale, the number returned is negative
                tribute_collected_parsed = str(format((tribute_collected*-1), '.2f')) + "k wxDAI"
                #tribute_collected_parsed = str(round((tribute_collected*-1), 2)) + "k wxDAI"
                amount_out = (amountBeforeTribute - tribute_collected) #we leave it negative for the supply calculations down below
                amount_out_parsed = str(format((amount_out*-1), '.2f')) + "k wxDAI" 
                #amount_out_parsed = str(round((amount_out*-1), 2)) + "k wxDAI"

                slippage = ((amount_in*(1-bondingCurve.exit_tribute))*bondingCurve.get_price(bondingCurve.current_supply) - amount_out) *-1
                slippage_pct = slippage / ((amount_in*(1-bondingCurve.exit_tribute))*bondingCurve.get_price(bondingCurve.current_supply)) *-1
                slippage_pct = str(format((slippage_pct*100), '.2f')) + "%"

                new_supply = max(
                    0, bondingCurve.current_supply + bondingCurve.purchase_return(amount_out),
                )

            new_price = bondingCurve.get_price(new_supply)
            new_price_parsed = str(format(new_price, '.2f')) + " wxDAI"
            #new_price_parsed = str(roud(new_price, 2)) + " wxDAI"
            new_balance = bondingCurve.get_balance(new_supply)

            # add to Dataframe
            outputTable.loc[len(outputTable.index)] = [
                (index+1),
                current_price,
                current_price_parsed,
                bondingCurve.current_supply,
                bondingCurve.current_balance,
                amount_in_parsed,
                tribute_collected_parsed,
                amount_out_parsed,
                new_price,
                new_price_parsed,
                new_supply,
                new_balance,
                slippage_pct,
            ]

            # update current supply and balance 
            bondingCurve.set_new_supply(new_supply)


        return outputTable

    def get_data_augmented_bonding_curve(self, bondingCurve, min_range, max_range, plot_mode=0):
        
        if plot_mode == 0:
            curve_draw = bondingCurve.curve_over_balance(min_range, max_range)
        elif plot_mode == 1:
            curve_draw = bondingCurve.curve_over_supply(min_range, max_range)
        
        return curve_draw

    def get_single_point_coordinates(self, steps_table):

        coord_list= []
        
        for index, row in steps_table.iterrows():
            #point = {'pointBalance' : row['currentBalance'], 'pointPrice': row['currentPrice'], 'pointSupply': row['currentSupply']}
            point = {'pointBalance' : row['currentBalance'], 'pointPrice': row['currentPrice']}
            coord_list.append(point)          
        
        last_row = steps_table.iloc[-1]
        #last_point = {'pointBalance' : last_row['newBalance'], 'pointPrice': last_row['newPrice'], 'pointSupply': row['newSupply']}
        last_point = {'pointBalance' : last_row['newBalance'], 'pointPrice': last_row['newPrice']}
        coord_list.append(last_point) 

        return coord_list

    def get_step_linspaces(self, bondingCurve, steps_table):

        linspace_list = []

        for index, row in steps_table.iterrows():
            lin_step = bondingCurve.curve_over_balance(bondingCurve.get_supply(row['currentBalance']), bondingCurve.get_supply(row['newBalance']), steps=100).to_dict(orient='list')
            #print("Interval:" + str(row['currentBalance']) + " - " + str(row['newBalance']))
            linspace_list.append(lin_step)

        return linspace_list


    def get_scenario_range(self, steps_table, zoom_graph=0):

        if steps_table.empty :
            min_range = 0
            max_range = 500
        else:
            min_range = 0 if  zoom_graph == 0 else ( min(steps_table['currentSupply'].min(), steps_table['newSupply'].min()) - 50)
            max_range = steps_table['newSupply'].max() + (200 if zoom_graph == 0 else 50)


        return [min_range, max_range]

    def get_milestone_table(self, bCurve):
        balance_list  = [250, 500, 1000, 2000, 3000, 5000, 10000]
        price_list = []
        supply_list = []

        for bal in balance_list:
            sup = bCurve.get_supply(bal)
            supply_list.append(sup)
            price_list.append(bCurve.get_price(sup))
        
        #print(balance_list)
        #print(price_list)
        #print(supply_list)

        table_data = { "balance": balance_list, "supply": supply_list, "price": price_list}

        #TO DO: See where to return it to
        return table_data

    def check_param_validity(self, commons_percentage, ragequit_percentage, opening_price, entry_tribute, exit_tribute,  scenario_reserve_balance,  steplist, zoom_graph, plot_mode):
        if commons_percentage < 0 or commons_percentage > 0.95:
            raise ValueError("Error: Invalid Commons Percentage Parameter.")
        if ragequit_percentage < 0 or ragequit_percentage > 0.20:
            raise ValueError("Error: Invalid Ragequit Percentage Parameter.")
        if opening_price <=0:
            raise ValueError("Error: Invalid Initial Price Parameter.")
        if entry_tribute < 0 or entry_tribute >= 1:
            raise ValueError("Error: Invalid Entry Tribute Parameter.")
        if exit_tribute < 0 or exit_tribute >= 1:
            raise ValueError("Error: Invalid Exit Tribute Parameter.")
        if scenario_reserve_balance <= 0:
            raise ValueError("Error: Invalid  Hatch Scenario Funding Parameter.")
        if not isinstance(steplist, list):
            #TO DO: in-depth validation of the steplist
            raise ValueError("Error: Invalid Steplist Parameter.")
        if not (zoom_graph == 0 or zoom_graph == 1):
            raise ValueError("Error: Invalid Graph Zoom Parameter.")
        if not (plot_mode == 0 or plot_mode == 1):
            raise ValueError("Error: Invalid Plot Mode Parameter.")
        
        return True

    