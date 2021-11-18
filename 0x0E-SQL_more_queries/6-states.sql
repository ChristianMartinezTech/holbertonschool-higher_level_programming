-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
