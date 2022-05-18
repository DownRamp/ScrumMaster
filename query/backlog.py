def backlog_fetch(cur):
    # go into db and grab backlog from query
    sql = """SELECT * FROM 
                 Tickets"""
    response = cur.execute(sql)
    return response.fetchall()

