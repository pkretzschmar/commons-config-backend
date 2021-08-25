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
        parser.add_argument('opening-price', type=float)
        parser.add_argument('token-freeze', type=float)
        parser.add_argument('token-thaw', type=float)
        parameters = parser.parse_args()
        opening_price = parameters['opening-price']
        token_freeze_period = parameters['token-freeze']
        token_thaw_period = parameters['token-thaw']

        token_lockup_model = TokenLockupModel(opening_price=opening_price,
                                              token_freeze_period=token_freeze_period,
                                              token_thaw_period=token_thaw_period)

        return jsonify(token_lockup_model.get_data())

class DisputableVoting(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('support-required', type=float)
        parser.add_argument('minimum-quorum', type=float)
        parser.add_argument('vote-duration', type=float)
        parser.add_argument('delegated-voting-period', type=float)
        parser.add_argument('quiet-ending-period', type=float)
        parser.add_argument('quiet-ending-extension', type=float)
        parser.add_argument('execution-delay', type=float)
        parameters = parser.parse_args()
        support_required = parameters['support-required']
        minimum_quorum = parameters['minimum-quorum']
        vote_duration = parameters['vote-duration']
        delegated_voting_period = parameters['delegated-voting-period']
        quiet_ending_period = parameters['quiet-ending-period']
        quiet_ending_extension = parameters['quiet-ending-extension']
        execution_delay = parameters['execution-delay']

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
        parser.add_argument('commons-percentage', type=float)
        parser.add_argument('ragequit-percentage', type=float)
        parser.add_argument('initial-price', type=float)
        parser.add_argument('entry-tribute', type=float)
        parser.add_argument('exit-tribute', type=float)
        parser.add_argument('hatch-scenario-funding', type=float)
        parser.add_argument('steplist', action='append')
        parser.add_argument('zoom-graph', type=int)
        parameters = parser.parse_args()
        commons_percentage = parameters['commons-percentage']
        ragequit_percentage = parameters['ragequit-percentage']
        initial_price = parameters['initial-price']
        entry_tribute = parameters['entry-tribute']
        exit_tribute = parameters['exit-tribute']
        hatch_scenario_funding = parameters['hatch-scenario-funding']
        #parse the steplist (which gets read as string) into the right format
        steplist = []
        for step in parameters['steplist']:
            buf = step.strip('][').split(', ')
            buf[0] = float(buf[0])
            buf[1] = buf[1].strip("'")
            steplist.append(buf)

        zoom_graph = parameters['zoom-graph']

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
