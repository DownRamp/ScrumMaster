
def parse_value(values):
    results = (values["title"], values["label_val"], values["description"], values["docs"],
    values["prty"], values["status"])
    return results

def parse_values(values, id):
    results = (values["title"], values["label_val"], values["description"], values["docs"],
    values["prty"], values["status"], id)
    return results

def save_ticket(values, conn):
    sql = """INSERT INTO Tickets("title", "label_val", "description", "docs", "prty", "status")
                 VALUES(%s, %s, %s, %s, %s, %s) RETURNING ticket_id;"""
    # insert into connections as well if possible
    parse_val = parse_value(values)
    cur = conn.cursor()
    cur.execute(sql, parse_val)
    conn.commit()
    return cur.fetchone()[0]


def update_ticket(values, id, conn):
    sql = """UPDATE Tickets
    SET title = (%s),
    label_val = (%s),
    description = (%s),
    docs = (%s),
    prty = (%s),
    status = (%s)
    WHERE ticket_id =(%s);"""
    parse_val = parse_values(values, id)
    cur = conn.cursor()
    response = cur.execute(sql, parse_val)
    conn.commit()
    return response

def fetch_ticket(id, conn):
    sql = """SELECT * FROM Tickets WHERE ticket_id=(%s)"""
    cur = conn.cursor()
    cur.execute(sql, id)
    return cur.fetchall()

def fetch_tickets(conn):
    sql = """SELECT * FROM Tickets"""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

