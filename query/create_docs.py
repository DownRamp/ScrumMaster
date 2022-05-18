def save_doc(values, conn, cur):
    sql = """INSERT INTO Documents
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURN doc_id;"""
    # insert into connections as well if possible
    response = cur.execute(sql, values)
    conn.commit()
    return cur.fetchone()[0]


def update_doc(values, id, conn, cur):
    sql = """UPDATE Documents 
    SET title = (%s),
    description = (%s),
    why = (%s),
    repo_conn = (%s)
    tests = (%s)
    devs = (%s)
    typ = (%s)
    WHERE doc_id =(%s);"""
    response = cur.execute(sql,values, id)
    conn.commit()
    return response

def fetch_doc(cur, id):
    sql = """SELECT * FROM Documents WHERE doc_id=(%s)"""
    response = cur.execute(sql, id)
    return response.fetchall()

def fetch_docs(cur):
    sql = """SELECT * FROM Documents"""
    response = cur.execute(sql)
    return response.fetchall()

def fetch_connections(cur):
    sql = """SELECT DISTINCT repo_conn FROM Documents"""
    response = cur.execute(sql)
    return response.fetchall()
