import requests
import json


class Doc:
    def __init__(self, title, description, why, repo_conn, tests, devs, types):
        self.title = title
        self.description = description
        self.why = why
        self.repo_conn = repo_conn
        self.tests = tests
        self.devs = devs
        self.types = types


def create(title, description, why, repo_conn, tests, devs, types):
    # return number
    url = 'localhost:8080/backlog/docs'
    cr_doc = Doc(title, description, why, repo_conn, tests, devs, types)
    body = json.dumps(cr_doc.__dict__)
    response = requests.post(url, body)
    return response
