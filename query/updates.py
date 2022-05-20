from datetime import date

def parse_values(values):
    results = (values["today"], values["yesterday"], values["today_work"], values["blockers"], values["full_name"])
    return results

# Scrum updates receive (post)
def save_updates(values, conn):
    sql = """INSERT INTO updates("today", "yesterday", "today_work", "blockers", "full_name")
                 VALUES(%s, %s, %s, %s, %s) RETURNING ticket_id;"""
    cur = conn.cursor()
    cur.execute(sql, parse_values(values))
    conn.commit()
    return cur.fetchone()[0]


# Fetch daily scrum updates (get)
def get_updates(conn):
    today = date.today()
    day = today.strftime("%d/%m/%Y")
    sql = f"SELECT * FROM updates WHERE today LIKE '{day}';"
    cur = conn.cursor()
    cur.execute(sql, day)
    return cur.fetchall()
