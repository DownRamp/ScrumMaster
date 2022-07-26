import requests
import json


def create(title, label_val, description, docs, status, prty, puml_txt):
    # return number
    url = 'http://localhost:8080/tickets'
    cr_tic = {
        "title": title,
        "label_val": label_val,
        "description": description,
        "docs": docs,
        "status": status,
        "prty": prty,
        "puml_txt": puml_txt
    }
    json_string = json.dumps(cr_tic)

    response = requests.post(url, data=json_string)
    return response.json()

def backlog():
    response = fetch()
    sprint = []
    next = []
    back = []
    for item in response:
        if item[4] == 1:
            sprint.append(item)
        elif item[4] == 2:
            next.append(item)
        else:
            back.append(item)

    return sprint, next, back

# backlog info
def fetch():
    # return number
    url = 'http://localhost:8080/tickets'
    response = requests.get(url)
    return response.json()


def fetch_id(id):
    url = f'http://localhost:8080/tickets/{id}'
    response = requests.get(url)
    return response.json()

# delete old tickets
def update(title, label_val, description, docs, status, prty, puml_txt, id):
    # return number
    url = f'http://localhost:8080/tickets/{id}'
    cr_tic = {
        "title": title,
        "label_val": label_val,
        "description": description,
        "docs": docs,
        "status": status,
        "prty": prty,
        "puml_txt": puml_txt
    }
    json_string = json.dumps(cr_tic)

    response = requests.put(url, data=json_string)
    return response.json()
