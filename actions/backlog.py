import requests


def sprint_fetch():
    # fetch sprint from api
    url = 'localhost:8080/backlog/sprint'
    response = requests.get(url)
    return response


def backlog_fetch():
    # go into db and grab backlog from api
    url = 'localhost:8080/backlog'
    response = requests.get(url)
    return response
