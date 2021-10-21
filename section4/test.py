import sqlite3

# Create a connection
connection = sqlite3.connect('data.db')

# create a cursor
cursor = connection.cursor()

# create a new table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# creaate a single user
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# create multiple users at once
users = [
    (2, 'rolf', '234'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, users)

# Quering a table
select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
