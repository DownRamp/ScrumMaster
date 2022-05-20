import requests
import json


class Ticket:
    def create(title, label_val, description, docs, status, prty, puml_txt):
        # return number
        url = 'localhost:8080/tickets'
        cr_tic = {
            "title": title,
            "label_val": label_val,
            "description": description,
            "docs": docs,
            "status": status,
            "prty": prty,
            "puml_txt": puml_txt
        }
        response = requests.post(url, data=cr_tic)
        return response

    def backlog():
        response = fetch()
        sprint = []
        next = []
        back = []
        for item in response:
            if item["status"] == 1:
                sprint.add(item)
            elif item["status"] == 2:
                next.add(item)
            else:
                back.add(item)

        return sprint, next, back

    # backlog info
    def fetch():
        # return number
        url = 'localhost:8080/tickets'
        response = requests.get(url)
        return response


    def fetch_id(id):
        url = f'localhost:8080/tickets/{id}'
        response = requests.get(url)
        return response

    # delete old tickets
    def update(title, label_val, description, docs, status, prty, puml_txt, id):
        # return number
        url = f'localhost:8080/tickets/{id}'
        cr_tic = {
            "title": title,
            "label_val": label_val,
            "description": description,
            "docs": docs,
            "status": status,
            "prty": prty,
            "puml_txt": puml_txt
        }
        response = requests.put(url, data=cr_tic)
        return response
