from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from models.token_lockup import TokenLockupModel

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
    def get(self):
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


api.add_resource(status, '/')
api.add_resource(TokenLockup, '/token-lockup/')

if __name__ == '__main__':
    app.run(debug=True)
