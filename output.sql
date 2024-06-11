Legitimate login attempt:
Executing query: SELECT * FROM users WHERE username = 'admin' AND password = 'admin123'
[(1, 'admin', 'admin123')]

SQL injection attempt:
Executing query: SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'
[(1, 'admin', 'admin123'), (2, 'user1', 'password1'), (3, 'user2', 'password2')]
