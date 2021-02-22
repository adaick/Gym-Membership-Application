import sqlite3

with sqlite3.connect("gymdatabase.db")as db:
    cursor = db.cursor()


cursor.execute("""DELETE FROM regimentype""")
db.commit()

cursor.execute("""
INSERT INTO regimentype(regimentype,monday,tuesday,wednesday,thursday,friday,saturday,sunday)
VALUES
("1","chest","biceps","rest","back","triceps","rest","rest"),
("2","chest","biceps","cardio/abs","back","triceps","leg","rest"),
("3","chest","biceps","cardio/abs","back","triceps","leg","cardio"),
("4","chest","biceps","cardio","back","triceps","cardio","cardio");
""")
db.commit()