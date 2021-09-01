from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json

from models.disputable_voting import DisputableVotingModel
from models.token_lockup import TokenLockupModel
from models.augmented_bonding_curve import BondingCurveHandler

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
        parser.add_argument('OpeningPrice', type=float)
        parser.add_argument('TokenFreeze', type=float)
        parser.add_argument('TokenThaw', type=float)
        parameters = parser.parse_args()
        opening_price = parameters['OpeningPrice']
        token_freeze_period = parameters['TokenFreeze']
        token_thaw_period = parameters['TokenThaw']

        token_lockup_model = TokenLockupModel(opening_price=opening_price,
                                              token_freeze_period=token_freeze_period,
                                              token_thaw_period=token_thaw_period)

        return jsonify(token_lockup_model.get_data())

class DisputableVoting(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('SupportRequired', type=float)
        parser.add_argument('MinimumQuorum', type=float)
        parser.add_argument('VoteDuration', type=float)
        parser.add_argument('DelegatedVotingPeriod', type=float)
        parser.add_argument('QuietEndingPeriod', type=float)
        parser.add_argument('QuietEndingExtension', type=float)
        parser.add_argument('ExecutionDelay', type=float)
        parameters = parser.parse_args()
        support_required = parameters['SupportRequired']
        minimum_quorum = parameters['MinimumQuorum']
        vote_duration = parameters['VoteDuration']
        delegated_voting_period = parameters['DelegatedVotingPeriod']
        quiet_ending_period = parameters['QuietEndingPeriod']
        quiet_ending_extension = parameters['QuietEndingExtension']
        execution_delay = parameters['ExecutionDelay']

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
        parser.add_argument('CommonsPercentage', type=float)
        parser.add_argument('RagequitPercentage', type=float)
        parser.add_argument('InitialPrice', type=float)
        parser.add_argument('EntryTribute', type=float)
        parser.add_argument('ExitTribute', type=float)
        parser.add_argument('HatchScenarioFunding', type=float)
        parser.add_argument('Steplist', action='append')
        parser.add_argument('ZoomGraph', type=int)
        parameters = parser.parse_args()
        commons_percentage = parameters['CommonsPercentage']
        ragequit_percentage = parameters['RagequitPercentage']
        initial_price = parameters['InitialPrice']
        entry_tribute = parameters['EntryTribute']
        exit_tribute = parameters['ExitTribute']
        hatch_scenario_funding = parameters['HatchScenarioFunding']
        #parse the steplist (which gets read as string) into the right format
        steplist = []
        for step in parameters['Steplist']:
            buf = step.strip('][').split(', ')
            buf[0] = float(buf[0])
            buf[1] = buf[1].strip("'")
            steplist.append(buf)

        zoom_graph = parameters['ZoomGraph']

        augmented_bonding_curve_model = BondingCurveHandler(
                commons_percentage= commons_percentage,
                ragequit_percentage= ragequit_percentage,
                initial_price=initial_price,
                entry_tribute=entry_tribute,
                exit_tribute=exit_tribute,
                hatch_scenario_funding=hatch_scenario_funding,
                steplist=steplist,
                zoom_graph= zoom_graph )

        
        return jsonify(augmented_bonding_curve_model.get_data())


api.add_resource(status, '/')
api.add_resource(TokenLockup, '/token-lockup/')
api.add_resource(DisputableVoting, '/disputable-voting/')
api.add_resource(AugmentedBondingCurve, '/augmented-bonding-curve/')

if __name__ == '__main__':
    app.run(debug=True)
