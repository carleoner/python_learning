'''
CREATE DATABASE ____
DROP DATABASE ____
SHOW DATABASES;
USE ____; -> select database to work with

CREATE TABLE user(userId int PRIMARY KEY, username varchar(10), email varchar(25), userType varchar(10));
DROP TABLE ___;
SHOW TABLES;

SELECT ... [WHERE / GROUP BY / HAVING cond / ORDER BY]
SELECT * from user

INSERT INTO user
VALUES(1545, "Pete", "pete@hot.com", "PRO dev");

SELECT userID, userType FROM user;

SELECT userID FROM user WHERE userType = "PRO dev";
SELECT * FROM user WHERE userType = "PRO dev";

'''

from unittest import result
from urllib import response
import mysql.connector

myDB = mysql.connector.connect(host = "localhost", 
        user = "root", passwd = "Howtobasics123!", database = "pythonx") # the last parameter is an option, one can write USE pythonx
myCursor = myDB.cursor()
myCursor.execute("INSERT INTO user VALUES(15, \"Pete\", \"pete@hot.com\", \"PRO dev\")")
myDB.commit()
myCursor.execute("SELECT * from user")
ret = myCursor.fetchall()
for i in ret:
    print(i)
myDB.close()