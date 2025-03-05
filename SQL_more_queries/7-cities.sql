-- This script creates table cities on a database 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    stat_id INT NOT NULL REFERENCES STATE(id),
    name VARCHAR(256) NOT NULL
)