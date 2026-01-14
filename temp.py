import pymongo
from bson.objectid import ObjectId 
from bson.json_util import dumps
import os 
import json
from datetime import datetime,date
import datetime
import hashlib
import datetime

MONGODB_URI = 'mongodb+srv://Pubzeee1311:12345@30daysofpython.xpenqyh.mongodb.net/'
client = pymongo.MongoClient(MONGODB_URI)
db = client['TrackmyClass']

today = datetime.now()
oneday = datetime.timedelta()

db.groups.insert_one({
    'gruopname': 'sec4',
    'events':{
        'temp': {
            'name': 'CP class'
            
        } ,
        'perm':  
    }
})