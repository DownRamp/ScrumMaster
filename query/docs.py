
def parse_value(values):
    #columns = list(first_record.keys())
    #sql_string += "(" + ', '.join(columns) + ")\nVALUES "
    results = (values["title"], values["description"],values["why"], values["repo_conn"], values["tests"],
    values["devs"], values["typ"])
    return results

def parse_values(values, id):
    #columns = list(first_record.keys())
    #sql_string += "(" + ', '.join(columns) + ")\nVALUES "
    results = (values["title"], values["description"],values["why"], values["repo_conn"], values["tests"],
    values["devs"], values["typ"], id)
    return results

def save_doc(values, conn):
    sql = """INSERT INTO Documents("title", "description", "why", "repo_conn", "tests", "devs", "typ")
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING doc_id"""
    # insert into connections as well if possible
    cur = conn.cursor()
    cur.execute(sql, parse_value(values))
    conn.commit()
    return cur.fetchone()[0]


def update_doc(values, id, conn):
    sql = """UPDATE Documents 
    SET title = (%s),
    description = (%s),
    why = (%s),
    repo_conn = (%s),
    tests = (%s),
    devs = (%s),
    typ = (%s)
    WHERE doc_id =(%s);"""
    cur = conn.cursor()
    cur.execute(sql, parse_values(values, id))
    conn.commit()
    return "SUCCESS"

def fetch_doc(id, conn):
    sql = """SELECT * FROM Documents WHERE doc_id=(%s)"""
    cur = conn.cursor()
    cur.execute(sql, id)
    return cur.fetchall()

def fetch_docs(conn):
    sql = """SELECT * FROM Documents"""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def fetch_connections(conn):
    sql = """SELECT DISTINCT repo_conn FROM Documents"""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()
