from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json

from models.disputable_voting import DisputableVotingModel
from models.token_lockup import TokenLockupModel
from models.augmented_bonding_curve import BondingCurveHandler
from models.conviction_voting import ConvictionVotingModel

app = Flask(__name__)
api = Api(app)
CORS(app)


class status(Resource):
    def get(self):
        try:
            return {'data': 'Api running'}
        except(error):
            return {'data': error}


class TokenLockup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('openingPrice', type=float)
        parser.add_argument('tokenFreeze', type=float)
        parser.add_argument('tokenThaw', type=float)
        parameters = parser.parse_args()
        opening_price = parameters['openingPrice']
        token_freeze_period = parameters['tokenFreeze']
        token_thaw_period = parameters['tokenThaw']

        token_lockup_model = TokenLockupModel(opening_price=opening_price,
                                              token_freeze_period=token_freeze_period,
                                              token_thaw_period=token_thaw_period)

        return jsonify(token_lockup_model.get_data())

class DisputableVoting(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('supportRequired', type=float)
        parser.add_argument('minimumQuorum', type=float)
        parser.add_argument('voteDuration', type=float)
        parser.add_argument('delegatedVotingPeriod', type=float)
        parser.add_argument('quietEndingPeriod', type=float)
        parser.add_argument('quietEndingExtension', type=float)
        parser.add_argument('executionDelay', type=float)
        parameters = parser.parse_args()
        support_required = parameters['supportRequired']
        minimum_quorum = parameters['minimumQuorum']
        vote_duration = parameters['voteDuration']
        delegated_voting_period = parameters['delegatedVotingPeriod']
        quiet_ending_period = parameters['quietEndingPeriod']
        quiet_ending_extension = parameters['quietEndingExtension']
        execution_delay = parameters['executionDelay']

        disputable_voting_model = DisputableVotingModel(support_required=support_required,
                                                        minimum_quorum=minimum_quorum,
                                                        vote_duration=vote_duration,
                                                        delegated_voting_period=delegated_voting_period,
                                                        quiet_ending_period=quiet_ending_period,
                                                        quiet_ending_extension=quiet_ending_extension,
                                                        execution_delay=execution_delay)

        return jsonify(disputable_voting_model.get_data())

class AugmentedBondingCurve(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('commonsTribute', type=float)
        parser.add_argument('ragequitPercentage', type=float)
        parser.add_argument('openingPrice', type=float)
        parser.add_argument('entryTribute', type=float)
        parser.add_argument('exitTribute', type=float)
        parser.add_argument('reserveBalance', type=float)
        parser.add_argument('initialBuy', type=float)
        parser.add_argument('stepList', action='append')
        parser.add_argument('zoomGraph', type=int)
        parameters = parser.parse_args()
        commons_percentage = parameters['commonsTribute'] if parameters['commonsTribute'] is not None else 0.05
        ragequit_percentage = parameters['ragequitPercentage'] if parameters['ragequitPercentage'] is not None else 0.05
        opening_price = parameters['openingPrice'] if parameters['openingPrice'] is not None else 3
        entry_tribute = parameters['entryTribute'] if parameters['entryTribute']  is not None else 0.05
        exit_tribute = parameters['exitTribute'] if parameters['exitTribute'] is not None else 0.05
        initial_buy = parameters['initialBuy'] if parameters['initialBuy'] is not None else 0
        scenario_reserve_balance = parameters['reserveBalance'] if parameters['reserveBalance'] is not None else 1571.22357
        #parse the steplist (which gets read as string) into the right format
        steplist = []
        if initial_buy > 0: 
            steplist.append([initial_buy, "wxDai"])
        if parameters['stepList']:
            for step in parameters['stepList']:
                buf = step.strip('][').split(', ')
                buf[0] = float(buf[0])
                buf[1] = buf[1].strip("'")
                steplist.append(buf)

        zoom_graph = parameters['zoomGraph'] if parameters['zoomGraph'] is not None else 0

        augmented_bonding_curve_model = BondingCurveHandler(
                commons_percentage= commons_percentage,
                ragequit_percentage= ragequit_percentage,
                opening_price=opening_price,
                entry_tribute=entry_tribute,
                exit_tribute=exit_tribute,
                scenario_reserve_balance=scenario_reserve_balance,
                steplist=steplist,
                zoom_graph= zoom_graph )

        
        return jsonify(augmented_bonding_curve_model.get_data())

class ConvictionVoting(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('spendingLimit', type=float)
        parser.add_argument('minimumConviction', type=float)
        parser.add_argument('convictionGrowth', type=int)
        parser.add_argument('convictionVotingPeriodDays', type=int)
        parameters = parser.parse_args()
        spending_limit = parameters['spendingLimit']
        minimum_conviction = parameters['minimumConviction']
        conviction_growth = parameters['convictionGrowth']
        voting_period_days = parameters['convictionVotingPeriodDays']

        conviction_voting_model = ConvictionVotingModel(
            spending_limit=spending_limit,
            minimum_conviction=minimum_conviction,
            conviction_growth=conviction_growth,
            voting_period_days=voting_period_days
        )

        return jsonify(conviction_voting_model.get_data())



api.add_resource(status, '/')
api.add_resource(TokenLockup, '/token-lockup/')
api.add_resource(DisputableVoting, '/disputable-voting/')
api.add_resource(AugmentedBondingCurve, '/augmented-bonding-curve/')
api.add_resource(ConvictionVoting, '/conviction-voting/')


if __name__ == '__main__':
    app.run(debug=True)
