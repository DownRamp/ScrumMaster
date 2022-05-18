import requests


def backlog_fetch():
    # go into db and grab backlog from query
    url = 'localhost:8080/backlog'
    response = requests.get(url)
    sprint = []
    backlog = []
    for tic in response:
        if tic[5] == 0:
            sprint.append(tic)
        else:
            backlog.append(tic)
    return sprint, backlog