import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Example function to fetch user data insecurely
def get_user_vulnerable(username, password):
    # Directly concatenating user inputs - This is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

# Example usage
username = input('Enter your username: ')
password = input('Enter your password: ')
user = get_user_vulnerable(username, password)

if user:
    print('Login successful')
else:
    print('Invalid credentials')

# Close the database connection
conn.close()
