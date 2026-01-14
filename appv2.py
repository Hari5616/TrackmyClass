import pymongo
from bson.objectid import ObjectId 
from bson.json_util import dumps
import os 
import json
from datetime import datetime,date
import datetime
import hashlib

ONGODB_URI = 'mongodb+srv://Pubzeee1311:12345@30daysofpython.xpenqyh.mongodb.net/'
client = pymongo.MongoClient(MONGODB_URI)
db = client['TrackmyClass']

def hash_pass(classified):
    hasher = hashlib.sha256()
    binary_classified = classified.encode('utf-8')
    hasher.update(binary_classified)
    return hasher.hexdigest()