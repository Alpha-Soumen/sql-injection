cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  age INTEGER)''')

cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Alice', 30))

connection.commit()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
