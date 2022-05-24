import requests
import json


def create(title, label_val, description):
    # return number
    url = 'http://localhost:8080/hiring'
    cr_hire = {
        "title" : title,
        "label_val": label_val,
        "description": description
    }
    response = requests.post(url, data=cr_hire)
    return response.json()

def fetch():
    # return number
    url = 'http://localhost:8080/hiring'
    response = requests.get(url)
    return response.json()