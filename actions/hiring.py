import requests
import json


class Hiring:
    def create(title, label_val, description):
        # return number
        url = 'localhost:8080/hiring'
        cr_hire = {
            "title" : title,
            "label_val": label_val,
            "description": description
        }
        response = requests.post(url, data=cr_hire)
        return response

    def fetch():
        # return number
        url = 'localhost:8080/hiring'
        response = requests.get(url)
        return response