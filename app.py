import pymongo
from bson.objectid import ObjectId 
from bson.json_util import dumps
import os 
import json
from datetime import datetime
import hashlib

MONGODB_URI = 'mongodb+srv://Pubzeee1311:jaijagat@30daysofpython.xpenqyh.mongodb.net/?appName=30daysofpython'
client = pymongo.MongoClient(MONGODB_URI)
db = client['TrackmyClass']

def hash(classified):
    hasher = hashlib.sha256()
    binary_classified = classified.encode('utf-8')
    hasher.update(binary_classified)
    return hasher.hexdigest()

def loginsignup():
    print("Welcome to TrackmyClass !!!\n")
    a = int(input("Enter 1 to login or 2 to sign up:"))
    if a == 1 : 
        b = int(input("Enter how do you want to login :\n1 for Student..\n2 for CR..\n3 for Admin..\n"))
        roles = [ "Student" , "CR" , "Admin" ]
        while 1:
            username = input("Enter Username:")
            password = input("Enter Password:")
            password = hash(password)
            user = db.users.find_one({"username" = username , "role" = roles[b] , password = password })
            if user == None :
                print("No such credentials found ...\nPlease try again.")
            else :
                print(f"You are logged in as {username} and role {user["role"]}.")
                    #goto dashboard(user)
                break
            
        
    if a == 2 :
        while 1:
            print("You are signing up as a Student.")
            username = input("Enter Username:")
            password = input("Enter Password:")
            password = hash(password)
            temp = list(db.students.find_one({"username" = username , "role" = "Student"}))
            if temp == None :
                student = {
                    "username" = username , 
                    "password" = password ,
                    "role" = "Student"
                }
                db.users.insert_one(student)
                break
            else :
                print("The username is taken. \nPlease try again..")
        

def dashboard(id):
    print("Welcome to the dashboard:")
    print("Enter '1' to access ")