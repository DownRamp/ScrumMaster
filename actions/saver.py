
class Ticket:
    def __init__(self, title, label_val, description, docs, status, prty, puml_txt):
        self.title = title
        self.label_val = label_val
        self.description = description
        self.docs = docs
        self.status = status
        self.prty = prty
        self.puml_txt = puml_txt

class Document:
    def __init__(self, title, description, why, repo_conn, tests, devs, types, puml_txt):
        self.title = title
        self.description = description
        self.why = why
        self.repo_conn = repo_conn
        self.tests = tests
        self.devs = devs
        self.types = types
        self.puml_txt = puml_txt
    def __str__(self):
        return f"{self.title}, {self.clean_puml(self.puml_txt)}"
    def clean_puml(self, puml_txt):
        return [p.replace("\\","").replace("'", "\"") for p in puml_txt]

class Updates:
    def __init__(self, today, yesterday, today_work, blockers, full_name):
        self.today = today
        self.yesterday = yesterday
        self.today_work = today_work
        self.blockers = blockers
        self.full_name = full_name

class Rolodex:
    def __init__(self, full_name, title, email):
        self.full_name = full_name
        self.title = title
        self.email = email

class Hiring:
    def __init__(self, title, label_val, description):
        self.title = title
        self.label_val = label_val
        self.description = description

doc_map = {}
tic_map = {}
hir_map = {}
rol_map = {}
upd_map = {}

# hold all current info
def docs():
    return doc_map

def tics():
    return tic_map

def hirs():
    return hir_map

def rols():
    return rol_map

def upds():
    return upd_map

# update current info
def update_hiring(hire, id):
    hir_map[id] = hire

def update_docs(doc, id):
    doc_map[id] = doc

def update_ticket(tic, id):
    tic_map[id] = tic

def update_rol(rol, id):
    rol_map[id] = rol

def update_upd(upd, id):
    upd_map[id] = upd