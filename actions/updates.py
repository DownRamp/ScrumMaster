import requests
import json


def create(today, yesterday, today_work, blockers, full_name):
    # return number
    url = 'http://localhost:8080/update'
    cr_upd = {
        "today": today,
        "yesterday": yesterday,
        "today_work": today_work,
        "blockers": blockers,
        "full_name": full_name
    }
    json_string = json.dumps(cr_upd)

    response = requests.post(url, data=json_string)
    return response.json()

def fetch():
    # return number
    url = 'http://localhost:8080/update'
    response = requests.get(url)
    return response.json()