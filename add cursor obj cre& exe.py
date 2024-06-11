cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  age INTEGER)''')

