# connect devs that worked and created docs and tickets
# create map topic and names (repo: Dev)

def parse_values(values):
    results = (values["full_name"], values["title"], values["email"])
    return results

def get_name(conn):
    sql = """SELECT * FROM rolodex"""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def post_name(values, conn):
    sql = """INSERT INTO rolodex("full_name", "title", "email")
                 VALUES(%s, %s, %s);"""
    cur = conn.cursor()
    cur.execute(sql, parse_values(values))
    conn.commit()
    return "SUCCESS"

