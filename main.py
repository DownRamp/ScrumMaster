from flask import Flask
from flask_restful import Api, reqparse
import pandas as pd
from database import connect
from API import Updates
from query import backlog, create_docs, create_tickets, fetch_docs, full_view, hiring, rolodex, sprint, updates


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
