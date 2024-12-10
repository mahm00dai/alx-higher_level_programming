-- move_to_utf8
-- Select the correct database
USE hbtn_0c_0;

-- Convert the database to UTF8 (utf8mb4, collation utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table first_table to UTF8 (utf8mb4, collation utf8mb4_unicode_ci)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the column 'name' in the first_table to UTF8 (collation utf8mb4_unicode_ci)
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL;
