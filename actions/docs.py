import requests
import json


class Doc:
    def create(title, description, why, repo_conn, tests, devs, types):
        # return number
        url = 'localhost:8080/docs'
        cr_doc = Doc(title, description, why, repo_conn, tests, devs, types)
        body = json.dumps(cr_doc.__dict__)
        response = requests.post(url, body)
        return response

