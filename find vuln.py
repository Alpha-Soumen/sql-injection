import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Example function to fetch user data securely
def get_user(username, password):
    # Use parameterized query to prevent SQL injection
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    return cursor.fetchone()

# Example usage
username = input('Enter your username: ')
password = input('Enter your password: ')
user = get_user(username, password)

if user:
    print('Login successful')
else:
    print('Invalid credentials')

# Close the database connection
conn.close()
