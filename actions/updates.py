import requests
import json


class Updates:
    def create(today, yesterday, today_work, blockers):
        # return number
        url = 'localhost:8080/update'
        cr_upd = {
            "today": today,
            "yesterday": yesterday,
            "today_work": today_work,
            "blockers": blockers
        }
        response = requests.post(url, data=cr_upd)
        return response

    def fetch():
        # return number
        url = 'localhost:8080/update'
        response = requests.get(url)
        return response