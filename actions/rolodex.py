import requests
import json


def create(full_name, title, email):
    # return number
    url = 'http://localhost:8080/rolodex'
    cr_rolo = {
        "full_name": full_name,
        "title": title,
        "email": email
    }
    json_string = json.dumps(cr_rolo)

    response = requests.post(url, data=json_string)
    return response.json()

def fetch():
    # return number
    url = 'http://localhost:8080/rolodex'
    response = requests.get(url)
    return response.json()