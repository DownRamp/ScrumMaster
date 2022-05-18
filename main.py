from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import pandas as pd
from database import connect
from query import backlog, create_docs, create_tickets, hiring, rolodex, updates
from datetime import date

class Backlog:
    def get(self):
        global cur
        return backlog.backlog_fetch(cur)

parser_doc = reqparse.RequestParser()
parser_doc.add_argument("title", type=str, help="Title of document")
parser_doc.add_argument("description", type=str, help="Description of document")
parser_doc.add_argument("why", type=str, help="Why the need for this new feature")
parser_doc.add_argument("repo_conn", type=str, help="How does this connect to other features")
parser_doc.add_argument("tests", type=str, help="Tests that need to made")
parser_doc.add_argument("devs", type=str, help="Devs with background knowledge")
parser_doc.add_argument("typ", type=str, help="type of document(new feature, addition, etc.)")

class Docs(Resource):
    def get(self):
        global cur
        return create_docs.fetch_docs(cur)

    def post(self):
        global cur, conn
        values = parser_doc.parse_args()
        return create_docs.save_doc(values, conn, cur)

class DocsId(Resource):
    def get(self, doc_id):
        global cur
        return create_docs.fetch_doc(cur, doc_id)

    def put(self, doc_id):
        global cur, conn
        values = parser_doc.parse_args()
        return create_docs.update_doc(values, doc_id, conn, cur)

class FullView(Resource):
    def get(self):
        global cur
        return create_docs.fetch_connections(cur)

parser_tic = reqparse.RequestParser()
parser_tic.add_argument("title", type=str, help="Title of document")
parser_tic.add_argument("label_val", type=str, help="What feature is this for")
parser_tic.add_argument("description", type=str, help="Description of ticket")
parser_tic.add_argument("docs", type=int, help="Document id connected")
parser_tic.add_argument("status", type=int, help="Tests that need to made")
parser_tic.add_argument("prty", type=str, help="Devs with background knowledge")

class Tickets(Resource):
    def get(self):
        global cur
        return create_tickets.fetch_tickets(cur)

    def post(self):
        global cur, conn
        values = parser_tic.parse_args()
        return create_docs.save_ticket(values, conn, cur)


class TicketsId(Resource):
    def get(self, ticket_id):
        global cur
        return create_tickets.fetch_ticket(cur, ticket_id)

    def put(self, ticket_id):
        global cur, conn
        values = parser_tic.parse_args()
        return create_docs.update_doc(values, ticket_id, conn, cur)

parser_hire = reqparse.RequestParser()
parser_hire.add_argument("title", type=str, help="Title of document")
parser_hire.add_argument("label_val", type=str, help="What feature is this for")
parser_hire.add_argument("description", type=str, help="Description of ticket")

class Hiring(Resource):
    def get(self):
        global cur
        return hiring.fetch(cur)

    def post(self):
        global cur, conn
        values = parse_hire.parse_args()
        return hiring.hire(values, conn, cur)

parser_rol = reqparse.RequestParser()
parser_rol.add_argument("names", type=str, help="Name")
parser_rol.add_argument("title", type=str, help="Job title")
parser_rol.add_argument("email", type=str, help="Email")

class Rolodex(Resource):
    def get(self):
        global cur
        return rolodex.get_name(cur)

    def post(self):
        global conn, cur
        values = parser_rol.parse_args()
        return rolodex.post_name(values, conn, cur)

parser_up = reqparse.RequestParser()
parser_up.add_argument("today", type=str, help="todays date")
parser_up.add_argument("yesterday", type=str, help="yesterdays work")
parser_up.add_argument("today_work", type=str, help="Todays work")
parser_up.add_argument("blockers", type=str, help="Blockers")

class Updates((Resource):
    def get(self):
        global cur
        today = date.today()
        day = today.strftime("%d/%m/%Y")
        return updates.get_updates(cur, day)

    def post(self):
        global cur, conn
        values = parser_up.parse_args()
        return updates.get_updates(values, conn, cur)

conn, cur = connect.connect()
app = Flask(__name__)
api = Api(app)
api.add_resource(Updates, '/update')
api.add_resource(Backlog, '/backlog')
api.add_resource(Docs, '/docs')
api.add_resource(DocsId, '/docs/<string:doc_id>')
api.add_resource(FullView, '/full')
api.add_resource(Tickets, '/tickets')
api.add_resource(TicketsId, '/tickets/<string:ticket_id>')
api.add_resource(Hiring, '/hiring')
api.add_resource(Rolodex, '/rolodex')

if __name__ == '__main__':
    app.run(debug=True)
