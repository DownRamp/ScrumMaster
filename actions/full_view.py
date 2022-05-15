# everytime a docs is created see how it is
# connected to other repos
# save puml
# update puml file

from plantuml import PlantUML
from os.path import abspath
import requests

# create a server object to call for your computations
server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                  basic_auth={},
                  form_auth={}, http_opts={}, request_opts={})

server.processes_file(abspath('./diagram.txt'))


def full_view():
    # fetch connections
    url = 'localhost:8080/backlog/full_view'
    response = requests.get(url)
    # generate puml file and create image

    # return image location

    location = "/"
    return location
