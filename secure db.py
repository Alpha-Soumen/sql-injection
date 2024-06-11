def secure_login(username, password):
    # Secure query using parameterized queries
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"Executing secure query: {query}")
    cursor.execute(query, (username, password))
    result = cursor.fetchall()
    return result

# Secure login attempt
print("\nSecure login attempt:")
secure_user = secure_login('admin', "' OR '1'='1")
print(secure_user)
