from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


class Report(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)
    parser.add_argument('state', type=dict)

    def post(self):
        args = self.parser.parse_args()
        print("ID: %s" % args["id"])
        print("State: ")
        print(args["state"])
        return 200


api.add_resource(Report, '/report')

if __name__ == '__main__':
    app.run(debug=True)
