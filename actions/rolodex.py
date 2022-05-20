import requests
import json


class Rolodex:
    def create(full_name, title, email):
        # return number
        url = 'localhost:8080/rolodex'
        cr_rolo = {
            "full_name": full_name,
            "title": title,
            "email": email
        }
        response = requests.post(url, data=cr_rolo)
        return response

    def fetch():
        # return number
        url = 'localhost:8080/rolodex'
        response = requests.get(url)
        return response