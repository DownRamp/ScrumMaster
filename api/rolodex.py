# connect devs that worked and created docs and tickets
# create map topic and names (repo: Dev)
def get_name():
    sql = """INSERT INTO vendors(vendor_name)
                 VALUES(%s) RETURNING vendor_id;"""

