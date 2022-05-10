# Accept requests to hire new staff internally
# e.g. need a new software engineer
# Create a job posting
# Group possible candidates
# filter resumes?

def hire():
    sql = """INSERT INTO Hiring
                 VALUES(%s) RETURNING vendor_id;"""
    # add roll and reason

