""" 
    Title: pytech_delete.py
"""
#Steven Spencer
#CYBR 410 T302
#January 30 2022
#pytech_delete.py

#import pymongo
from pymongo import MongoClient

#connect with URL
url = "mongodb+srv://admin:admin@cluster0.huyp4.mongodb.net/pytech?retryWrites=true&w=majority"

#connect to MongoDB
client = MongoClient(url)

#connect to the pytech database
db = client.pytech

#get the student collection 
students = db.students

#list all the students 
student_list = students.find({})

print("\n  - Displaying Students From The Database Using Find()- ")

#loop for all the students to print out
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#testing input
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

#using insert_one to put in the student document 
test_doc_id = students.insert_one(test_doc).inserted_id

 
print("\n  - Inserted Statement - ")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

#finding the inserted document by ID
student_test_doc = students.find_one({"student_id": "1010"})

#displaying find results
print("\n  - Display Student Test Document- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

#deleting the student by ID 1010
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

#finding all students again to verify deletion
new_student_list = students.find({})

# display message 
print("\n  - Displaying Students From find() -")

#loop to print out students
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#exit program
input("\n\n  End of program, press any key to continue...")
