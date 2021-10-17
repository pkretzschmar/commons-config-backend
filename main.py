from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

from models.disputable_voting import DisputableVotingModel
from models.token_lockup import TokenLockupModel
from models.augmented_bonding_curve import BondingCurveHandler
from models.issue_generator import IssueGeneratorModel
from models.conviction_voting import ConvictionVotingModel

app = Flask(__name__)
api = Api(app)
CORS(app)
load_dotenv() 


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
        parser.add_argument('ragequitAmount', type=float)
        parser.add_argument('openingPrice', type=float)
        parser.add_argument('entryTribute', type=float)
        parser.add_argument('exitTribute', type=float)
        parser.add_argument('reserveBalance', type=float)
        parser.add_argument('initialBuy', type=float)
        parser.add_argument('stepList', action='append')
        parser.add_argument('virtualSupply', type=float)
        parser.add_argument('virtualBalance', type=float)
        parser.add_argument('zoomGraph', type=int)
        parameters = parser.parse_args()
        commons_percentage = parameters['commonsTribute'] if parameters['commonsTribute'] is not None else 0.05
        ragequit_amount = parameters['ragequitAmount'] if parameters['ragequitAmount'] is not None else 0
        opening_price = parameters['openingPrice'] if parameters['openingPrice'] is not None else 1.50
        entry_tribute = parameters['entryTribute'] if parameters['entryTribute']  is not None else 0.05
        exit_tribute = parameters['exitTribute'] if parameters['exitTribute'] is not None else 0.05
        scenario_reserve_balance = parameters['reserveBalance'] if parameters['reserveBalance'] is not None else 1571.22357
        initial_buy = parameters['initialBuy'] if parameters['initialBuy'] is not None else 0 
        virtual_supply = parameters['virtualSupply'] if parameters['virtualSupply'] is not None else 2035.918945  
        virtual_balance = parameters['virtualBalance'] if parameters['virtualBalance'] is not None else 1571.22357         
        steplist = parameters['stepList'] if parameters['stepList'] is not None else ""
        zoom_graph = parameters['zoomGraph'] if parameters['zoomGraph'] is not None else 0

        augmented_bonding_curve_model = BondingCurveHandler(
                commons_percentage= commons_percentage,
                ragequit_amount= ragequit_amount,
                opening_price=opening_price,
                entry_tribute=entry_tribute,
                exit_tribute=exit_tribute,
                initial_buy=initial_buy,
                scenario_reserve_balance=scenario_reserve_balance,
                virtual_supply= virtual_supply,
                virtual_balance= virtual_balance,
                steplist=steplist,
                zoom_graph= zoom_graph )

        
        return jsonify(augmented_bonding_curve_model.get_data())

class IssueGenerator(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('overallStrategy', type=str)
        parser.add_argument('tokenLockup', type=dict)
        parser.add_argument('augmentedBondingCurve', type=dict)
        parser.add_argument('taoVoting', type=dict)
        parser.add_argument('convictionVoting', type=dict)
        parser.add_argument('advancedSettings', type=dict)

        parameters = parser.parse_args()
        title = parameters['title']
        overall_strategy = parameters['overallStrategy']
        token_lockup = parameters['tokenLockup']
        abc = parameters['augmentedBondingCurve']
        tao_voting = parameters['taoVoting']
        conviction_voting = parameters['convictionVoting']
        advanced_settings = parameters['advancedSettings']

        issue_generator = IssueGeneratorModel(
            raw_body=parameters,
            title=title,
            token_lockup=token_lockup,
            abc=abc,
            tao_voting=tao_voting,
            conviction_voting=conviction_voting,
            advanced_settings=advanced_settings,
            overall_strategy=overall_strategy
        )

        return jsonify(issue_generator.generate_output())

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

class ImportParams(Resource):
    def get(self):
        MONGODB_CLIENT = os.getenv('MONGODB_CLIENT')
        client = MongoClient(MONGODB_CLIENT)
        db = client.get_database('test_tec_params_db')
        test_params_db = db.test_params
        parser = reqparse.RequestParser()
        parser.add_argument('issueNumber', type=int)
        parameters = parser.parse_args()
        issue_number = parameters.get('issueNumber', '')
        issue_data = test_params_db.find_one({'issue_number':issue_number})
        issue_data.pop('_id', None)

        return jsonify(issue_data)


api.add_resource(status, '/')
api.add_resource(ImportParams, '/import-parameters/')
api.add_resource(TokenLockup, '/token-lockup/')
api.add_resource(DisputableVoting, '/disputable-voting/')
api.add_resource(AugmentedBondingCurve, '/augmented-bonding-curve/')
api.add_resource(IssueGenerator, '/issue-generator/')
api.add_resource(ConvictionVoting, '/conviction-voting/')


if __name__ == '__main__':
    app.run(debug=True)
