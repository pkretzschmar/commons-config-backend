from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json

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
api.add_resource(AugmentedBondingCurve, '/augmented-bonding-curve/')

if __name__ == '__main__':
    app.run(debug=True)
