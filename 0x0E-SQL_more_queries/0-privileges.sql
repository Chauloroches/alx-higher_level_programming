-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost)

-- Create the users 
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant some privileges 
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT, UPDATE ON *.* TO 'user_0d_2'@'localhost';

-- Flush privileges to update changes
FLUSH PRIVILEGES;

-- List all privileges for user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
