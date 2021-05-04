import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

create_table_users =  "CREATE TABLE IF NOT EXISTS  users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_users)

create_table_houses =  create_table_users =  "CREATE TABLE IF NOT EXISTS  houses (id INTEGER PRIMARY KEY, name text)"
cursor.execute(create_table_houses)

conn.commit()
conn.close()