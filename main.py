from flask import Flask
from flask_restful import Api, reqparse
import pandas as pd
from database import connect
from api import backlog, create_docs, create_tickets, fetch_docs, full_view, hiring, rolodex, sprint, updates


class Updates:
    def get(self):
        global cur
        updates.get_updates(cur)

    def post(self):
        global cur
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
        updates.save_updates(cur, new_data)


class Sprint:
    def get(self):
        global cur
        sprint.gen_sprint(cur)


class Backlog:
    def get(self):
        global cur
        backlog.sprint_fetch(cur)

class Docs:
    def get(self):
        global cur
        backlog.sprint_fetch(cur)


class Tickets:
    def get(self):
        global cur
        backlog.sprint_fetch(cur)


class Hiring:
    def get(self):
        global cur
        backlog.sprint_fetch(cur)


class Rolodex:
    def get(self):
        global cur
        backlog.sprint_fetch(cur)


cur = connect.connect()
app = Flask(__name__)
api = Api(app)
api.add_resource(Updates, '/update')
api.add_resource(Backlog, '/backlog')
api.add_resource(Docs, '/docs')
api.add_resource(Tickets, '/tickets')
api.add_resource(Hiring, '/hiring')
api.add_resource(Sprint, '/sprint')
api.add_resource(Backlog, '/backlog')
api.add_resource(Rolodex, '/rolodex')


if __name__ == '__main__':
    app.run()
