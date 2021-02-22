import sqlite3


    
# deleting regimen from the database by its type
def delete_regimen():
    regimentype = int(input("Enter regimen type :- "))
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    delete = ("""DELETE FROM regimentype where regimentype = ?""")
    cursor.execute(delete,[regimentype])
    db.commit()

def view_regimen():
    print("Following are the regimen by their types. For BMI>18.5 - TYPE 1, BMI>25 - TYPE 2, BMI>30 - TYPE 3, BMI<30 - TYPE 4")
    print("They are listed by the day. From MONDAY to SUNDAY")
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM regimentype ")
    regimentype = cursor.fetchall()
    print(type(regimentype))
    print(regimentype)
    print("\n")

    if regimentype:
        for j in regimentype:
            
            print("\nTYPE :- ")
            for i in j:
                print(i, end=' ')
                print()
                # print("\nMONDAY :- ",regimentype[i][2])
                # print("\nTUESDAY :- ",regimentype[i][3])
                # print("\nWEDNESDAY :- ",regimentype[i][4])
                # print("\nTHURSDAY :- ",regimentype[i][5])
                # print("\nFRIDAY :- ",regimentype[i][6])
                # print("\nSATURDAY :- ",regimentype[i][7])
                # print("\nSUNDAY :- ",regimentype[i][8])
                
            
    else:
        print("No REGIMEN TYPE found")

# creating regimen for the user according to their BMI
def regimen():

    username = input("Enter Username :- ")
    BMI = int(input("Enter User's BMI :- "))
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    regimentype = 0
    if BMI < int(18.5):
        regimentype = regimentype + 1
        return  regimentype
    elif BMI < 25:
        regimentype = regimentype + 2
        return regimentype
    elif BMI < 30:
        regimentype = regimentype + 3
        return regimentype
    else:
        regimentype = regimentype + 4
        return regimentype


    user_reg = """INSERT INTO userregimen(username,BMI,regimentype)
    values(?,?,?)"""
    cursor.execute(add_user, [(username),(BMI),(regimentype)])
    db.commit()
    print("Thank you for successfully creating a user regimen :)")