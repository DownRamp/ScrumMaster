from PIL import Image
from plantuml import PlantUML
from os.path import abspath
from saver import docs

def process_puml(path):
    try:
        server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                                  basic_auth={},
                                  form_auth={}, http_opts={}, request_opts={})
        server.processes_file(abspath(f"./{path}.txt"))
    except e:
        print(e)

def create_puml(name, value):
    if name is None or value is None:
        return
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

def create_full_puml(name, value):
    documents = docs()
    if name is None or value is None:
        return
    path = "../Diagrams/"+name
    file = open(path+".txt","w+")
    file.write("' http://tonyballantyne.com/graphs.html#orgheadline19\n")
    file.write("' http://graphviz.org/doc/info/shapes.html\n")
    file.write("\n")
    file.write('(*) --> "User" as user\n')
    inner = []
    flag = True
    for conn in value:
        # Get names
        main_title = documents.get(conn[0]).title
        # start connection string
        file.write(f'user --> "{main_title}" as {main_title}\n')
        if flag:
            inner.append(f'{main_title} --> "internal resource" as internal\n')
            flag = False
        else:
            inner.append(f"{main_title} --> internal\n")

        for index, i in enumerate(conn[1]):
            # Write connection string
            inner_title = documents.get(i).title
            inner.append(f"    --> {inner_title}\n")

    for i in inner:
        file.write(i)

    file.write(f"internal --> (*)")
    file.close()
    process_puml(path)
    image = Image.open(path+".png")
    return image
