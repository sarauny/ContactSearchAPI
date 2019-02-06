import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()

# cur.execute("Select * from search_contact limit 5;")
cur.execute("PRAGMA table_info('search_company');")
# names = list(map(lambda x: x[0], cur.description))
# names = [description[0] for description in cur.description]


results = cur.fetchall()

# print(names)
print(results)