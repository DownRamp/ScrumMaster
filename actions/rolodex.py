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
    response = requests.post(url, data=cr_rolo)
    return response.json()

def fetch():
    # return number
    url = 'http://localhost:8080/rolodex'
    response = requests.get(url)
    return response.json()