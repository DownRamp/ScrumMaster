
# generate sprint

def gen_sprint(cur):
    # Get highest priority first
    # Get metrics (Current Velocity)
    sql = """INSERT INTO vendors(vendor_name)
                 VALUES(%s) RETURNING vendor_id;"""
    response = cur.ex


