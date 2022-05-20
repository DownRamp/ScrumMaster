
def parse_values(values):
    results = (values["title"], values["label_val"], values["description"])
    return results

def fetch(conn):
    sql = """SELECT * FROM hire"""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def hire(values, conn):
    cur = conn.cursor()
    sql = """INSERT INTO hire("title", "label_val", "description")
                 VALUES(%s, %s, %s) RETURNING hire_id;"""
    cur.execute(sql, parse_values(values))
    conn.commit()
    return cur.fetchone()[0]

