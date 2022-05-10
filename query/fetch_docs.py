def fetch(cur):
    sql = """SELECT * from Documents;"""
    cur.execute(sql)