-- SQL script to create table id_not_null.

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
