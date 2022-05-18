# Scrum updates receive (post)
def save_updates(values, conn, cur):
    sql = """INSERT INTO Updates
                 VALUES(%s, %s, %s, %s) RETURNING ticket_id;"""
    response = cur.execute(sql, values)
    conn.commit()
    return cur.fetchone()[0]


# Fetch daily scrum updates (get)
def get_updates(cur, new_date):
    sql = """SELECT * FROM Updates WHERE today=(%s)"""
    response = cur.execute(sql, new_date)
    return response.fetchall()
