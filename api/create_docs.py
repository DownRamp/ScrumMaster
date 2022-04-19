from flask import Flask

# fill in thing
# store
# repo created?
# repo connected to another. Call full_view


def save_doc(cur):
    sql = """INSERT INTO Documents
                 VALUES(%s) RETURNING vendor_id;"""
    # insert into connections as well if possible
    return "Success"

def update_doc(cur):
    sql = """UPDATE Documents 
    SET title = (%s)
        
    WHERE doc_id =(%s);"""
    response = cur.execute(sql)
    return response
    # Release instructions
    # Installation Guide
    # End-user guides

