import requests


def sprint_fetch():
    # fetch sprint from query
    url = 'localhost:8080/backlog/sprint'
    response = requests.get(url)
    return response


def backlog_fetch():
    # go into db and grab backlog from query
    url = 'localhost:8080/backlog'
    response = requests.get(url)
    return response
