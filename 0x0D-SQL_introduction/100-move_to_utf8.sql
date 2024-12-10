-- move_to_utf8
-- Select the correct database
USE hbtn_0c_0;
-- Convert the entire database to utf8mb4 charset and utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table 'first_table' to utf8mb4 charset and utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the 'name' field in 'first_table' to utf8mb4 charset and utf8mb4_unicode_ci collation
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
