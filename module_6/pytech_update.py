""" 
pytech_update.py

"""
#Steven Spencer
#January 30 2022
#pytech_update.py
#CYBR 410 T302

#import pymongo
from pymongo import MongoClient

#connection to URL
url = "mongodb+srv://admin:admin@cluster0.huyp4.mongodb.net/cybr?retryWrites=true&w=majority"

#connect to the client
client = MongoClient(url)

#connect to pytech database
db = client.pytech

#get the student collection
students = db.students

#list all the student documents
student_list = students.find({})


print("\n  - Displaying Students from Query -")

#loop to get all the students
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#call update to change last name of 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Potts"}})

#find the updated student by id 1007 
tony = students.find_one({"student_id": "1007"})

#print header
print("\n  - Displaying Student Id 1007- ")

#print out the students
print("  Student ID: " + tony["student_id"] + "\n  First Name: " + tony["first_name"] + "\n  Last Name: " + tony["last_name"] + "\n")

#exit program
input("\n\n  End of program, press any key to continue...")
