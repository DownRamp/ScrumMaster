# Accept requests to hire new staff internally
# e.g. need a new software engineer
# Create a job posting
# Group possible candidates
# filter resumes?

deg fetch(cur):
    sql = """SELECT * FROM Hire"""
    response = cur.execute(sql)
    return response.fetchall()

def hire(values, conn, cur):
    sql = """INSERT INTO Hire
                 VALUES(%s, %s, %s) RETURNING hire_id;"""
    response = cur.execute(sql, values)
    conn.commit()
    return cur.fetchone()[0]

