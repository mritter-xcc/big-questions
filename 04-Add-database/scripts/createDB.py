import sqlite3

# db name variable
DB = 'meaning-life.db'

# connect to db - create if not exist
con = sqlite3.connect(DB)
# create cursor to interact with db
cur = con.cursor() 

# create db table
cur.execute("""
    CREATE TABLE comments
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        title TEXT,
        comment TEXT
    )
""")

# execute the query
con.commit()
# close db connection
con.close()