import requests
import json


class Ticket:
    def __init__(self, title, label_val, description, docs, priority):
        self.title = title
        self.label_val = label_val
        self.description = description
        self.docs = docs
        self.priority = priority


def create(title, label_val, description, docs, priority):
    # return number
    url = 'localhost:8080/backlog/ticket'
    cr_ticket = Ticket(title, label_val, description, docs, priority)
    body = json.dumps(cr_ticket.__dict__)
    response = requests.post(url, body)
    return response
