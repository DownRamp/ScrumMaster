
# Spit out one or multiple tickets
# Handle higher priority tickets
# Check weighing


def backlog_fetch(cur):
    # go into db and grab backlog from query
    sql = """SELECT * FROM 
                 Tickets Where status = 0"""
    response = cur.execute(sql)
    return response

