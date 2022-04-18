from flask import Flask
from flask_restful import Api, reqparse
import pandas as pd
from database import connect


class Updates:
    def get(self):
        print()

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        # Create a 2 week sprint
        # Trigger check ins
        # Handel incoming requests Start API
        # Check and store velocity
        print()


connect.connect()
app = Flask(__name__)
api = Api(app)
api.add_resource(Updates, '/update')
# api.add_resource(Backlog, '/backlog')
# api.add_resource(Docs, '/docs')
# api.add_resource(Tickets, '/tickets')
# api.add_resource(Hiring, '/hiring')
# api.add_resource(Sprint, '/sprint')
# api.add_resource(Backlog, '/backlog')
# api.add_resource(Rolodex, '/rolodex')


if __name__ == '__main__':
    app.run()
