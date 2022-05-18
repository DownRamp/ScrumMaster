# connect devs that worked and created docs and tickets
# create map topic and names (repo: Dev)
def get_name(cur):
    sql = """SELECT * FROM Rolodex"""
    response = cur.execute(sql)
    return response.fetchall()

def post_name(values, conn, cur):
    sql = """INSERT INTO Rolodex
                 VALUES(%s, %s, %s);"""
    cur.execute(sql, values)
    conn.commit()
    return "SUCCESS"

