# fill in a thing
# store in db

def create(cur):
    sql = """INSERT INTO Tickets
                 VALUES(%s) RETURNING vendor_id;"""
    cur.execute(sql)

