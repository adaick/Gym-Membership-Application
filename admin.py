import time
import sqlite3
import user
import regimen

def menu():
    print("******WELCOME TO ADMIN MENU******")
    
    while(True):
        choice = int(input("""
        Please choose from the following:
    
        1. Add Member/User
        2. View Member
        3. Delete Member
        4. Update Member
        5. Create Regimen for Member
        6. View Regimen
        7. Delete Regimen
        8. Exit
    
        """))
        if choice == 1:
            user.new_user()

        if choice == 2:
            user.view_user()

        if choice == 3:
            user.delete_user()

        if choice == 4:
            user.update_user()

        if choice == 5:
            regimen.regimen()

        if choice == 6:
            regimen.view_regimen()

        if choice == 7:
            regimen.delete_regimen()

        if choice == 8:
            exit()