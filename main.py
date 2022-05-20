from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import pandas as pd
from database import connect
from query import create_docs, create_tickets, hiring, rolodex, updates


parser_doc = reqparse.RequestParser()
parser_doc.add_argument("title", type=str, help="Title of document")
parser_doc.add_argument("description", type=str, help="Description of document")
parser_doc.add_argument("why", type=str, help="Why the need for this new feature")
parser_doc.add_argument("repo_conn", type=str, help="How does this connect to other features")
parser_doc.add_argument("tests", type=str, help="Tests that need to made")
parser_doc.add_argument("devs", type=str, help="Devs with background knowledge")
parser_doc.add_argument("typ", type=str, help="type of document(new feature, addition, etc.)")

class Docs(Resource):
    global conn
    def get(self):
        global cur
        return create_docs.fetch_docs(conn)

    def post(self):
        values = parser_doc.parse_args()
        return create_docs.save_doc(values, conn)

class DocsId(Resource):
    global conn
    def get(self, doc_id):
        return create_docs.fetch_doc(doc_id, conn)

    def put(self, doc_id):
        values = parser_doc.parse_args()
        return create_docs.update_doc(values, doc_id, conn)

class FullView(Resource):
    global conn
    def get(self):
        return create_docs.fetch_connections(conn)

parser_tic = reqparse.RequestParser()
parser_tic.add_argument("title", type=str, help="Title of document")
parser_tic.add_argument("label_val", type=str, help="What feature is this for")
parser_tic.add_argument("description", type=str, help="Description of ticket")
parser_tic.add_argument("docs", type=int, help="Document id connected")
parser_tic.add_argument("status", type=int, help="Tests that need to made")
parser_tic.add_argument("prty", type=str, help="Devs with background knowledge")

class Tickets(Resource):
    global conn
    def get(self):
        return create_tickets.fetch_tickets(conn)

    def post(self):
        values = parser_tic.parse_args()
        return create_tickets.save_ticket(values, conn)


class TicketsId(Resource):
    global conn
    def get(self, ticket_id):
        return create_tickets.fetch_ticket(ticket_id, conn)

    def put(self, ticket_id):
        values = parser_tic.parse_args()
        return create_tickets.update_ticket(values, ticket_id, conn)

parser_hire = reqparse.RequestParser()
parser_hire.add_argument("title", type=str, help="Title of document")
parser_hire.add_argument("label_val", type=str, help="What feature is this for")
parser_hire.add_argument("description", type=str, help="Description of ticket")

class Hiring(Resource):
    global conn
    def get(self):
        return hiring.fetch(conn)

    def post(self):
        values = parser_hire.parse_args()
        return hiring.hire(values, conn)

parser_rol = reqparse.RequestParser()
parser_rol.add_argument("full_name", type=str, help="Name")
parser_rol.add_argument("title", type=str, help="Job title")
parser_rol.add_argument("email", type=str, help="Email")

class Rolodex(Resource):
    global conn
    def get(self):
        return rolodex.get_name(conn)

    def post(self):
        values = parser_rol.parse_args()
        return rolodex.post_name(values, conn)

parser_up = reqparse.RequestParser()
parser_up.add_argument("today", type=str, help="todays date")
parser_up.add_argument("yesterday", type=str, help="yesterdays work")
parser_up.add_argument("today_work", type=str, help="Todays work")
parser_up.add_argument("blockers", type=str, help="Blockers")

class Updates(Resource):
    global conn

    def get(self):
        return updates.get_updates(conn)

    def post(self):
        values = parser_up.parse_args()
        return updates.save_updates(values, conn)

conn = connect.connect()
app = Flask(__name__)
api = Api(app)
api.add_resource(Updates, '/update')
api.add_resource(Docs, '/docs')
api.add_resource(DocsId, '/docs/<string:doc_id>')
api.add_resource(FullView, '/full')
api.add_resource(Tickets, '/tickets')
api.add_resource(TicketsId, '/tickets/<string:ticket_id>')
api.add_resource(Hiring, '/hiring')
api.add_resource(Rolodex, '/rolodex')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
