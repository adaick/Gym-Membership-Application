import sqlite3

# creating the database for the gym if it doesn't exist

with sqlite3.connect("gymdatabase.db")as db:
    cursor = db.cursor()

# creating the table for users if it doesn't exist

cursor.execute("""
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
fullname VARCHAR(20) NOT NULL,
age VARCHAR(20) NOT NULL,
gender VARCHAR(20) NOT NULL,
mobile VARCHAR(20) NOT NULL,
email VARCHAR(50) NOT NULL,
BMI VARCHAR(20) NOT NULL,
membership VARCHAR(20) NOT NULL);
""")
db.commit()

# creating the table for admin if it doesn't exist

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
adminID INTEGER PRIMARY KEY,
adminname VARCHAR(20) NOT NULL,
mobile VARCHAR(20) NOT NULL);
""")
db.commit()

# creating the table for regimentype if it doesn't exist

cursor.execute("""
CREATE TABLE IF NOT EXISTS regimentype(
regimentypeID INTEGER PRIMARY KEY,
regimentype VARCHAR(20) NOT NULL,
monday VARCHAR(20) NOT NULL,
tuesday VARCHAR(20) NOT NULL,
wednesday VARCHAR(20) NOT NULL,
thursday VARCHAR(20) NOT NULL,
friday VARCHAR(50) NOT NULL,
saturday VARCHAR(20) NOT NULL,
sunday VARCHAR(20) NOT NULL);
""")
db.commit()

# creating the table for userregimen if it doesn't exist

cursor.execute("""
CREATE TABLE IF NOT EXISTS userregimen(
regimenID INTEGER PRIMARY KEY,
username INTEGER NOT NULL,
BMI VARCHAR(20) NOT NULL,
regimentype VARCHAR(10),
FOREIGN KEY(regimentype) REFERENCES regimentype(regimentype),
FOREIGN KEY(username) REFERENCES user(username));
""")
db.commit()


## TEST CODES












# cursor.execute(""" INSERT INTO user(username,fullname,age,gender,mobile,email,BMI,membership)
# VALUES("adaick","ADARSH MALLICK","20","M","123456","123456@ajhd.com","20","1")""")
# db.commit()

cursor.execute(""" INSERT INTO userregimen(username,BMI,regimentype)
VALUES("adaick","20","2")""")
db.commit()

cursor.execute(""" INSERT INTO admin(adminname,mobile)
VALUES("Mallick","1212121212")""")
db.commit()