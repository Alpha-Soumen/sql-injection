-- Create users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Insert sample data into users table
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
INSERT INTO users (username, password) VALUES ('user1', 'password1');
INSERT INTO users (username, password) VALUES ('user2', 'password2');

-- Create categories table
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Insert sample data into categories table
INSERT INTO categories (name) VALUES ('Technology');
INSERT INTO categories (name) VALUES ('Health');
INSERT INTO categories (name) VALUES ('Lifestyle');

-- Create posts table
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Insert sample data into posts table
INSERT INTO posts (user_id, category_id, title, content) VALUES (1, 1, 'First Post', 'This is the content of the first post.');
INSERT INTO posts (user_id, category_id, title, content) VALUES (2, 2, 'Health Tips', 'This is some health-related content.');
INSERT INTO posts (user_id, category_id, title, content) VALUES (3, 3, 'Lifestyle Hacks', 'This is some lifestyle content.');

-- Create comments table
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert sample data into comments table
INSERT INTO comments (post_id, user_id, content) VALUES (1, 2, 'Great post!');
INSERT INTO comments (post_id, user_id, content) VALUES (2, 3, 'Very informative.');
INSERT INTO comments (post_id, user_id, content) VALUES (3, 1, 'Thanks for the tips!');
