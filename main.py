from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)


class status(Resource):
    def get(self):
        try:
            return {'data': 'Api running'}
        except(error):
            return {'data': error}


api.add_resource(status, '/')


if __name__ == '__main__':
    app.run(debug=True)
