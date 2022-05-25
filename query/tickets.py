
def parse_value(values):
    results = (values["title"], values["label_val"], values["description"], values["docs"],
    values["prty"], values["status"], values["puml_txt"])
    return results

def parse_values(values, id):
    results = (values["title"], values["label_val"], values["description"], values["docs"],
    values["prty"], values["status"], values["puml_txt"], id)
    return results

def save_ticket(values, conn):
    sql = """INSERT INTO Tickets("title", "label_val", "description", "docs", "prty", "status", "puml_txt")
                 VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING ticket_id;"""
    # insert into connections as well if possible
    parse_val = parse_value(values)
    cur = conn.cursor()
    cur.execute(sql, parse_val)
    conn.commit()
    return cur.fetchone()[0]


def delete_ticket(id, conn):
    sql = """DELETE FROM Tickets WHERE ticket_id = %s;"""
    cur = conn.cursor()
    response = cur.execute(sql, id)
    conn.commit()
    return response

def move_ticket(values, conn):
    sql = """INSERT INTO Old_tickets("title", "label_val", "description", "docs", "prty", "status", "puml_txt")
             VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING ticket_id;"""
    # delete or move
    cur = conn.cursor()

    cur.execute(sql, parse_value(values))
    conn.commit()
    return ""

def update_ticket(values, id, conn):

    if(values["status"] == 0):
        move_ticket(values, conn)
        return delete_ticket(id, conn)
    else:
        return real_update(values, id, conn)

def real_update(values, id, conn):
        sql = """UPDATE Tickets
        SET title = (%s),
        label_val = (%s),
        description = (%s),
        docs = (%s),
        prty = (%s),
        status = (%s)
        puml_txt = (%s)

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

