-- a script that creates the database hbtn_0d_usa and the table cities
-- CREATE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL FOREIGN KEY REFERENCES id.states,
name VARCHAR(256) NOT NULL);
