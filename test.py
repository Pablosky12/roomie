import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "steve", "asdf")
insert = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert, user)

users = [(2, "pepe", "asdf"), (3, "maria", "asdf")]

cursor.executemany(insert, users)

select = "SELECT * FROM users"

for row in cursor.execute(select):
    print(row)


conn.commit()
conn.close()