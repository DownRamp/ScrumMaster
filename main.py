from flask import Flask
from flask_restful import Api, Resource, request, abort, fields, marshal_with
from database import connect
from query import docs, tickets, rolodex, updates
import json

class Docs(Resource):
    global conn
    def get(self):
        global cur
        return docs.fetch_docs(conn)

    def post(self):
        values = json.loads(request.data)
        print(values)
        return docs.save_doc(values, conn)

class DocsId(Resource):
    global conn
    def get(self, doc_id):
        return docs.fetch_doc(doc_id, conn)

    def put(self, doc_id):
        values = json.loads(request.data)
        return docs.update_doc(values, doc_id, conn)

class FullView(Resource):
    global conn
    def get(self):
        return docs.fetch_connections(conn)

class Tickets(Resource):
    global conn
    def get(self):
        return tickets.fetch_tickets(conn)

    def post(self):
        values = json.loads(request.data)
        return tickets.save_ticket(values, conn)

class TicketsId(Resource):
    global conn
    def get(self, ticket_id):
        return tickets.fetch_ticket(ticket_id, conn)

    def put(self, ticket_id):
        values = json.loads(request.data)
        return tickets.update_ticket(values, ticket_id, conn)

class Rolodex(Resource):
    global conn
    def get(self):
        return rolodex.get_name(conn)

    def post(self):
        values = json.loads(request.data)
        return rolodex.post_name(values, conn)

class Updates(Resource):
    global conn

    def get(self):
        return updates.get_updates(conn)

    def post(self):
        values = json.loads(request.data)
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
api.add_resource(Rolodex, '/rolodex')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
