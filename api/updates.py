

# Scrum updates receive (post)
#
def save_updates(cur):
    sql = """INSERT INTO vendors(vendor_name)
                 VALUES(%s) RETURNING vendor_id;"""
    cur.execute(sql)


# Fetch daily scrum updates (get)
#
def get_updates(cur, new_data):
    sql = """INSERT INTO vendors(vendor_name)
                 VALUES(%s) RETURNING vendor_id;"""
    cur.execute(sql, (new_data[0], new_data[1]))
