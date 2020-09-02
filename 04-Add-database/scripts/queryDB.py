import sqlite3

# db name variable
DB = 'meaning-life.db'

# connect to db - create if not exist
con = sqlite3.connect(DB)
# create cursor to interact with db
cur = con.cursor() 

# create db table
cur.execute("""
    SELECT * FROM comments
""")

# get returned results
data = cur.fetchall()
# view data returned
print(data)

# execute the query
con.commit()
# close db connection
con.close()
