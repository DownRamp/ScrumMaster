from PIL import Image
from plantuml import PlantUML
from os.path import abspath

def process_puml(path):
    try:
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                                  basic_auth={},
                                  form_auth={}, http_opts={}, request_opts={})

        server.processes_file(abspath(f"./{path}.txt"))
    except e:
        print(e)

example = ["\\(\\*\\)\\ \\-\\->\\ 'User'\\ as\\ user\\", "user\\ \\-\\->\\ 'Website'\\ as\\ web\\", "user\\ \\-\\->\\ 'Sprint\\ update\\ \\(POST\\)'\\ as\\ upsprint\\", "web\\ \\-\\->\\ 'Create\\ doc\\ \\(POST\\)'\\ as\\ doc\\", "\\ \\ \\ \\ \\-\\->\\ 'API'\\ as\\ api\\", "web\\ \\-\\->\\ 'Create\\ ticket\\ \\(POST\\)'\\ as\\ ticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Update\\ doc\\ \\(POST\\)'\\ as\\ updoc\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Update\\ ticket\\ \\(POST\\)'\\ as\\ upticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Hiring\\ \\(POST\\)'\\ as\\ ticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Fetch\\ sprint\\ updates\\ \\(GET\\)'\\ as\\ sprint\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Backlog\\ \\(GET\\)'\\ as\\ ticket\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Fetch\\ full\\ view\\ \\(GET\\)'\\ as\\ full\\", "\\ \\ \\ \\ \\-\\->\\ 'Create\\ puml'\\ as\\ puml\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Rolodex\\ \\(GET\\)'\\ as\\ rolo\\", '\\ \\ \\ \\ \\-\\->\\ api\\', "web\\ \\-\\->\\ 'Show\\ docs\\ \\(GET\\)'\\ as\\ show\\", '\\ \\ \\ \\ \\-\\->\\ puml\\', '\\ \\ \\ \\ \\-\\->\\ api\\', 'api\\ \\-\\->\\ \\(\\*\\)']
def create_puml(name, value):
    # line by line
    path = "../Diagrams/"+name
    file = open(path+".txt","w+")
    file.write("' http://tonyballantyne.com/graphs.html#orgheadline19\n")
    file.write("' http://graphviz.org/doc/info/shapes.html\n")
    file.write("\n")
    for line in example:

        file.write(line.replace("\\","").replace("'", "\"")+"\n")
    file.close()
    process_puml(path)
    image = Image.open(path+".png")
    return image

create_puml("example",example)