#Title: what_a_book.py
#Author:Steven Spencer with Select assistance from Professor Krasso, and CYBR410 T301 Week 10 Code Snippets for Requirements (Jason Kramer)
#Date:March 1st 2022
#Program Purpose:WhatABook program for a book store, displays a menu with four options, allows for viewing books in the database, store locations
#customer account, and exiting the program. Customer account has a nested menu that takes the input as a customer id, then the user, if valid, can 
#view current books on their wishlist, addbooks to their wishlist, or return to the main menu. Includes error catch for non existent database
#and invalid user. Local machine use, so no true authentication, only customer id matching with the database.
#Database must be created first using MySQL client on localhost using CREATE DATABASE whatabook;
#whatabook_init must be run before program execution

import sys
import mysql.connector
from mysql.connector import errorcode

#database config
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
#create methods for show_menu, show_books(_cursor), show_all_locations(_cursor), validation_of_user(), show_account_menu()
#show_wishlist(_cursor, _user_id), show_books_to_add(_cursor, _user_id), add_book_to_wishlist(_cursor, _user_id, _book_id) 
#as required by business rules and requirements.

#show_menu() method as required
def show_menu():
    print("\n  ---- Main Menu ---- \n")
    print("    1. View Current Books\n    2. View All Store Locations\n    3. My Customer Account\n    4. Exit Program")

    try:
        choice = int(input('\n   <Example Enter: 1 for Current Book Listings>: '))
        return choice
#error code for invalid entry using ValueError builtin for entry outside of bounds
    except ValueError:
        print("\n  Invalid Entry has been Entered , Program has been Terminated... \n")
        print("\n  Have a Wonderful Day!  ")
        sys.exit(0)

#show_all_locations(_cursor) method as required
def show_all_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()

#Print all current store locations
    print("\n  ---- DISPLAYING ALL CURRENT STORE LOCATIONS ---- \n")

#for loop to show all the locations, and print to screen
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#show_books(_cursor) method as required
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()

#print the books in the database
    print("\n  ---- DISPLAYING ALL CURRENT BOOK LISTINGS ----- \n")
    
    #for loop to show all the books, and print to screen
    for book in books:
        print(" Book Id: {}\n Book Name: {}\n Author: {}\n Description: {}\n".format(book[0], book[1], book[2], book[3]))


#validation_of_user() method as required
def validation_of_user():
    
    #try block to get valid customer id number, otherwise return an error
    try:
        user_id = int(input('\n      Enter a Valid Customer Identification Number <Example 1 for Customer ID 1, or 2 for Customer ID 2 >: '))

     #limited if statement for the program boundaries, would need modification if expanded customer IDs, print errors, exit program if invalid
        if user_id <= 0  or user_id > 3:
            print("\n   You Entered An Invalid Customer Identification Number, Program has been Terminated...\n")
            print("\n   Have a Wonderful Day! \n ******************************** \n  ")
            sys.exit(0)
        return user_id

    #ValueError catch for invalid number, print errors, exit program
    except ValueError:
        print("\n  Invalid Number Entered, Program has been Terminated...\n")
        print("\n   Have a Wonderful Day! \n ************************************* \n  ")
        sys.exit(0)

#show_account_menu() method as required
def show_account_menu():

    #try block to print options for customer menu, and validate input
    try:
        print("\n     ---- Customer Menu ---- ")
        print("        1. My Wishlist\n        2. Add Book\n        3. Main Menu ")
        account_option = int(input('        <Example Enter: 1 for  My Wishlist, or 2 for Add Book >: '))
        while account_option > 0 and account_option < 4:
                return account_option
        else:
                print("\n Invalid Input, Please Retry.. \n")
                account_option = show_account_menu()
    
    #ValueError catch for invalid number, print error, exit program
    except ValueError:
        print("\n  Invalid Number Entered, Program has been Terminated..\n")
        print("\n   Have a Wonderful Day! \n ************************************* \n ")
        sys.exit(0)

#show_wishlist(_cursor, _user_id) method as required
def show_wishlist(_cursor, _user_id):

    #Inner Join commands to get wishlist based on the selected and prior validated user
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()

    #print header for current wishlist items
    print("\n      ---- DISPLAYING ALL CURRENT WISHLIST ITEMS ---- \n")

#for loop to display current books in the wishlist as previously input by program direction
    for book in wishlist:
        print("   Book Id: {}\n   Book Name: {}\n   Author: {}\n".format(book[3], book[4], book[5]))

#show_books_to_add(_cursor, _user_id) method as required
def show_books_to_add(_cursor, _user_id):

    #make a query to select the books from book using code snippet provided in program guidance CYBR 410
    query = ("SELECT book_id, book_name, author, details " +
            "FROM book " +
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    _cursor.execute(query)
    #fetchall()
    books_to_add = _cursor.fetchall()

    #print header for displaying available books
    print("\n      ---- DISPLAYING ALL AVAILABLE BOOKS TO ADD ---- \n")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n        Author: {}\n        Description: {}\n".format(book[0], book[1], book[2], book[3]))

#add_book_to_wishlist(_cursor, _user_id, _book_id) method as required, to be called in main script, db commit in script
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


#Main program, try/catch/exception block - try accesses all required methods, except addresses connection error and username/password for local user error
try:

    #connection snippet as provided in program guidelines using config block, allows use of cursor in database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

#print program header
    print("\n    -- Welcome to the WhatABook Application Bookstore! -- ")
    print(" \n ********************************************* ")
    #using show_menu() method, initialize user_select variable integer
    user_select = show_menu()
    #limited user_select variable due to program constraints, 3 users !=4
    while user_select != 4:

        #user_select 1, utilize show_books method
        if user_select == 1:
            show_books(cursor)

        #user_select 2, utilize show_all_locations method
        if user_select == 2:
            show_all_locations(cursor)

        #user_select 3, invoke validation_of_user method, allow show_account_menu, error handling is in show_account_menu method
        if user_select == 3:
            my_user_id = validation_of_user()
            account_option = show_account_menu()

            #while loop as long as input is != 3 which is menu return
            while account_option != 3:

                #account_option 1 chosen, show wishlist of the current user
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #account_option 2 chosen, show books not in user wishlist, allow input of book ID to add, add to current user wishlist, commit and output to customer
                if account_option == 2:
                    #call show_books_to_add method using current id
                    show_books_to_add(cursor, my_user_id)
                    #receive input of book Id
                    book_id = int(input("\n      Enter the Identification Number of the Book You Wish to Add: "))
                    if book_id <= 0 or book_id > 8:
                        print("\n   Invalid Book Identification Number, Please Try Again ...")
                        print("\n ************************************************ ")
                        account_option = show_account_menu()

                    #call add_book_to_wishlist(cursor, my_user_id, book_id)
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #commit wishlist changes, and output to user
                    db.commit()
                    print("\n      Book Identification Number: {} was added to your wishlist!".format(book_id))

                #validate account_option selection is within bounds, if not display error message and return user to show_account_menu 
                if account_option < 0 or account_option > 3:
                    print("\n    Invalid Option was Selected, Please Try Again... \n")
                    print("\n ***************************************************** \n")
                account_option = show_account_menu()
        
        #invoke boundaries on user_select, return user to show_menu
        if user_select < 0 or user_select > 4:
            print("\n   You Entered An Invalid Option, Please Make A Different Selection...  \n")
        user_select = show_menu()

    #If exit program selected
    print("\n Program Has Been Terminated .. \n *********************************** \n")
    sys.exit(0)

#mysql error statements
except mysql.connector.Error as err:
    #invalid authenticated username/password using er_access_denied_error
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The Username or Password Entered is Invalid ")
    #elif database error using er_bad_db_error
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The Selected Database Does Not Exist ")
    #else output generic error message
    else:
        print(err)
#close database connection
finally:
    db.close()
