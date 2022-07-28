import requests
import json
from actions import saver
#from saver import update_docs, Document

def multi_update_saver(responses):
    for i in responses:
        saver.update_docs(saver.Document(i[1], i[2], i[3], i[8], i[4], i[5], i[6], i[7]),i[0])

def update_saver(title, description, why, repo_conn, tests, devs, types, puml_txt, id):
    saver.update_docs(saver.Document(title, description, why, repo_conn, tests, devs, types, puml_txt),id)

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
    update_saver(title, description, why, repo_conn, tests, devs, types, puml_txt, response.json())
    return response.json()

def fetch():
    # return number
    url = 'http://localhost:8080/docs'
    response = requests.get(url)
    multi_update_saver(response.json())
    return response.json()

def fetch_conn():
    # return number
    url = 'http://localhost:8080/full'
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
    update_saver(title, description, why, repo_conn, tests, devs, types, puml_txt, id)

    return response.json()
