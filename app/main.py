from flask_restful import Resource, Api, reqparse
from Models import Device, db
from app import app

api = Api(app)


class Report(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)
    parser.add_argument('state', type=dict)

    def post(self):
        args = self.parser.parse_args()
        dev = Device(name=args["id"])
        db.session.merge(dev)
        db.session.commit()
        return


api.add_resource(Report, '/report')

if __name__ == '__main__':
    app.run(debug=True)
