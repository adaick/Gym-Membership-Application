##
import time
import sqlite3
import user
import admin




def menu():
    print("******************WELCOME TO YOUR GYM******************")
    print ("\n")
    print ("\n")
    print ("1. ADMIN")
    print ("2. USER")
    print ("3. EXIT")
    print ("\n")

menu()

while(True):
    input = int(input("Choose Your Option :- "))
    if input == 1:
        admin.menu()

    if input == 2:
        user.menu()

    if input == 3:
        exit()