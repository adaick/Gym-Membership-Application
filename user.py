import time
import sqlite3

# function to allow user to login to the system by their username
def user_login():
    for i in range(1, 3):
        username = input("Enter your username:- ")

        with sqlite3.connect("gymdatabase.db")as db:
            cursor = db.cursor()
        check = ("SELECT * FROM user WHERE username = ? ")
        cursor.execute(check, [username])
        valid_user = cursor.fetchall()


        if valid_user:
            display()

# creating new user 
def new_user():
    print("Add new user")
    time.sleep(1)

    #  checking username isn't already in use
    flag = False
    while not flag:
        username = input("Please enter your preferred username ")
        with sqlite3.connect("gymdatabase.db")as db:
            cursor = db.cursor()
        clash = ("SELECT * FROM user WHERE username = ?")
        
        cursor.execute(clash, [username])
        if cursor.fetchall():
            print("Sorry, this username is already taken, please try another one :( ")
        else:
            flag = True

    fullname = input("Please enter your full name:- ")
    age = input("Please enter your age:- ")
    gender = input("Please enter your gender:- ")
    mobile = input("Please enter your mobile:- ")
    email = input("Please enter your email:- ")
    BMI = input("Please enter your BMI:- ")
    membership = input("Please enter membership( 1, 3, 6 or 12 months):- ")
    
    add_user = """INSERT INTO user(username,fullname,age,gender,mobile,email,BMI,membership)
    values(?,?,?,?,?,?,?,?)"""
    cursor.execute(add_user, [(username),(fullname),(age),(gender),(mobile),(email),(BMI),(membership)])
    db.commit()
    print("Thank you for successfully creating a user account :)")

# viewing user details by their mobile number
def view_user():
    mobile = input("Enter your mobile:- ")

    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    check = ("SELECT fullname, age, mobile, membership FROM user WHERE mobile = ? ")
    cursor.execute(check, [mobile])
    valid_user = cursor.fetchall()
    #print(type(valid_user))
    #print(valid_user[0][1])
    print("\n")
    if valid_user:
        print("\nNAME :- ",valid_user[0][0])
        print("\nAGE :- ",valid_user[0][1])
        print("\nMOBILE :- ",valid_user[0][2])
        print("\nMEMBERSHIP :- ",valid_user[0][3])
    else:
        print("No Member found")

# deleting user from the database
def delete_user():
    username = input("Enter your username:- ")
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    delete = ("""DELETE FROM user where username = ?""")
    cursor.execute(delete,[username])
    db.commit()

# updating user's membership details
def update_user():
    username = input("Enter your username:- ")
    membership = input("Please enter membership( 0, 1, 3, 6 or 12 months):- ")
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    update = ("""UPDATE user SET membership = ? where username = ?""")
    cursor.execute(update,[membership,username])
    db.commit()


# user can see their regimen details 
def myreg():
    username = input("\n Enter username :- ")
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    query = ("""SELECT user.fullname, user.age, userregimen.regimentype, regimentype.monday, regimentype.tuesday, regimentype.wednesday, regimentype.thursday, regimentype.friday, regimentype.saturday, regimentype.sunday
    FROM user INNER JOIN (userregimen INNER JOIN regimentype ON userregimen.regimentype = regimentype.regimentype) ON user.username = userregimen.username
    WHERE (((user.username)=?));""")
    cursor.execute(query, [(username)])
    results = cursor.fetchall()
    print("Following are the regimen by their types. For BMI>18.5 - TYPE 1, BMI>25 - TYPE 2, BMI>30 - TYPE 3, BMI<30 - TYPE 4")
    print()
    
    for line in results:
        
        print("Hey WELCOME :- ",line[0])
        print("AGE : ",line[1])
        print("Regimen Type : ",line[2])
        print("Your Exercises are following :-")
        print("Monday :",line[3])
        print("Tuesday :",line[4])
        print("Wednesday :",line[5])
        print("Thursday :",line[6])
        print("Friday :",line[7])
        print("Saturday :",line[8])
        print("Sunday :",line[9])
        print("")


def myprofile():
    username = input("\n Enter username :- ")
    with sqlite3.connect("gymdatabase.db")as db:
        cursor = db.cursor()
    query = ("""SELECT user.fullname, user.age, user.mobile, user.email, user.membership, userregimen.regimentype
    FROM user INNER JOIN userregimen ON user.username = userregimen.username
    WHERE (((user.username)=?));""")
    cursor.execute(query, [(username)])
    results = cursor.fetchall()
    #print(results)
    for line in results:
        
        print("Hey WELCOME :- ",line[0])
        print("AGE : ",line[1])
        print("Mobile : ",line[2])
        print("E-Mail :",line[3])
        print("Membership (in months) :",line[4])
        print("Regimen Type :",line[5])
        print("")


def menu():
    print("******WELCOME TO USER MENU******")


    while(True):
        choice = int(input("""
        Please choose from the following:
    
        1 - Login to existing account
        2 - Exit
    
        """))

        if choice == 1:
            user_login()

        if choice == 2:
            exit()
        

def display():
    while(True):
        choice = int(input("""
        Please choose from the following:
    
        1 - My Regimen
        2 - My Profile
        3 - Exit
    
        """))
        if choice == 1:
            myreg()

        if choice == 2:
            myprofile()

        if choice == 3:
            exit()