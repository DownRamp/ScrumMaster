import requests
import json


def create(title, description, why, repo_conn, tests, devs, types, puml_txt):
    # return number
    url = 'http://localhost:8080/docs'
    cr_doc = {
        "title": title,
        "description": description,
        "why": why,
        "repo_conn": repo_conn,
        "tests": tests,
        "devs": devs,
        "typ": types,
        "puml_txt": puml_txt
    }
    json_string = json.dumps(cr_doc)
    response = requests.post(url, data=json_string)
    return response.json()

def fetch():
    # return number
    url = 'http://localhost:8080/docs'
    response = requests.get(url)
    return response.json()

def fetch_conn():
    # return number
    url = 'http://localhost:8080/full_view'
    response = requests.get(url)
    return response.json()

def fetch_id(id):
    url = f'http://localhost:8080/docs/{id}'
    response = requests.get(url)
    return response.json()

def update(title, description, why, repo_conn, tests, devs, types, puml_txt, id):
    # return number
    url = f'http://localhost:8080/docs/{id}'
    cr_doc = {
        "title": title,
        "description": description,
        "why": why,
        "repo_conn": repo_conn,
        "tests": tests,
        "devs": devs,
        "typ": typ,
        "puml_txt": puml_txt
    }
    json_string = json.dumps(cr_doc)
    response = requests.put(url, data=json_string)
    return response.json()
