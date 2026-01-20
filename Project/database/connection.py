from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
#Need toconnnect Mongo Db and return ..database..
def get_database():
    client= MongoClient(os.getenv("MONGO_URL"))
    return client['TrackMyClass']
    

#Get a specific collection from database, arguement is the collections name
def get_collection(name):
    db=get_database()
    return db[name]



