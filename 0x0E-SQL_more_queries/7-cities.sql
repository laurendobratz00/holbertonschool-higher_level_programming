-- a script that creates the database hbtn_0d_usa and the table cities
-- CREATE
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL AUTO_INCREMENT,
UNIQUE(id),
PRIMARY KEY(id),
state_id INT NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
name VARCHAR(256) NOT NULL);
