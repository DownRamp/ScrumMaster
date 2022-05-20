
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
def fetch_data():
    print()

# update current info
def update_data():
    print()
