""" pytech_insert.py """
##pytech_insert
##Steven Spencer
## CYBR 410 T 302 Winter 2021

##import Mongo for py
from pymongo import MongoClient
## connection value passed to url variable
url = "mongodb+srv://admin:admin@cluster0.huyp4.mongodb.net/cybr?retryWrites=true&w=majority"
## connecting to the MongoDB
client = MongoClient(url)
##connect to the specified database
db = client.pytech

###insert data on students
tony = {
    "student_id": "1007",
    "first_name": "Tony",
    "last_name": "Stark",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2022",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Intro to DB",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Smith",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# thor student
thor = {
    "student_id": "1008",
    "first_name": "Thor",
    "last_name": "Thunder",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2021",
            "end_date": "September 14, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Intro to DB",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Smith",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# stephen strange student
strange = {
    "student_id": "1009",
    "first_name": "Stephen",
    "last_name": "Strange",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2021",
            "end_date": "September 14, 2021",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Intro to DB",
                    "instructor": "Professor Smith",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}
#get database
students = db.students

#insert statement
print("/n -Insert Statement -")
tony_student_id = students.insert_one(tony).inserted_id
print(" Inserted student record Tony Stark into the student collection document with document_id " + str(tony_student_id))

thor_student_id = students.insert_one(thor).inserted_id
print(" Inserted student record Thor Thunder into the student collection document with document_id " + str(thor_student_id))

strange_student_id = students.insert_one(strange).inserted_id
print(" Inserted student record Stephen Strange into the student collection document with document_id " + str(strange_student_id))

input("\n\n  End of program, press any key to exit... ")
