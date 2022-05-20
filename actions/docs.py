import requests
import json


class Doc:
    def create(title, description, why, repo_conn, tests, devs, types):
        # return number
        url = 'localhost:8080/docs'
        cr_doc = {
            "title": title,
            "description": description,
            "why": why,
            "repo_conn": repo_conn,
            "tests": tests,
            "devs": devs,
            "typ": typ
        }
        response = requests.post(url, data=cr_doc)
        return response

    def fetch():
        # return number
        url = 'localhost:8080/docs'
        response = requests.get(url)
        return response

    def fetch_conn():
        # return number
        url = 'localhost:8080/full_view'
        response = requests.get(url)
        return response

    def fetch_id(id):
        url = f'localhost:8080/docs/{id}'
        response = requests.get(url)
        return response

    def update(title, description, why, repo_conn, tests, devs, types, id):
        # return number
        url = f'localhost:8080/docs/{id}'
        cr_doc = {
            "title": title,
            "description": description,
            "why": why,
            "repo_conn": repo_conn,
            "tests": tests,
            "devs": devs,
            "typ": typ
        }
        response = requests.put(url, data=cr_doc)
        return response
