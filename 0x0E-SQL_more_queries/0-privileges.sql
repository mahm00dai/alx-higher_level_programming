-- 0-privileges.sql
-- Create user_0d_2 if it doesn't exist
--CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to user_0d_2 if necessary
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- List the privileges of user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List the privileges of user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
