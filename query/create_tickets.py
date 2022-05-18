
def save_ticket(values, conn, cur):
    sql = """INSERT INTO Tickets
                 VALUES(%s, %s, %s, %s, %s, %s);"""
    # insert into connections as well if possible
    response = cur.execute(sql, values)
    conn.commit()
    return cur.fetchone()[0]


def update_ticket(values, id, conn, cur):
    sql = """UPDATE Tickets
    SET title = (%s),
    label_val = (%s),
    description = (%s),
    docs = (%s)
    status = (%s)
    prty = (%s)
    WHERE doc_id =(%s);"""
    response = cur.execute(sql, values, id)
    conn.commit()
    return response

def fetch_ticket(cur, id):
    sql = """SELECT * FROM Tickets WHERE ticket_id=(%s)"""
    response = cur.execute(sql, id)
    return response.fetchall()

def fetch_tickets(cur):
    sql = """SELECT * FROM Tickets"""
    response = cur.execute(sql)
    return response.fetchall()

