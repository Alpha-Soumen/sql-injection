import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Function to simulate user login
def login(username, password):
    # Insecure SQL query vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing query: {query}")
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Attempt to login with legitimate credentials
print("Legitimate login attempt:")
legit_user = login('admin', 'admin123')
print(legit_user)

# Attempt to login with SQL injection
print("\nSQL injection attempt:")
injection_user = login('admin', "' OR '1'='1")
print(injection_user)

# Close the database connection
conn.close()
