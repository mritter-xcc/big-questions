import sqlite3

# db name variable
DB = 'meaning-life.db'

# connect to db - create if not exist
con = sqlite3.connect(DB)
# create cursor to interact with db
cur = con.cursor() 

# create db table
cur.execute("""
    INSERT INTO comments (name, title, comment) VALUES 
    ('Justin Example', 'Its All in a Number', '42'),
    ('Lora Norda', 'See the World!', 'Experience all there is to experience.'),
    ('Syd Down', 'Fairytale', 'To live happily ever after.')
""")

# execute the query
con.commit()
# close db connection
con.close()