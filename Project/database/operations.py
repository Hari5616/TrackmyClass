from connection import get_collection

#arguent are collection_name and the document we want to insert, return the inserted_id
def insert_one(collection_name,document):
    collection=get_collection(collection_name)
    result=collection.insert_one(document)
    return result.inserted_id

#same as above
def insert_many(collection_name,document):
    collection=get_collection(collection_name)
    result=collection.insert_many(document)
    return result.inserted_id
    

#Find one document in collection,arguement is collection_name and querry
def find_one(collection_name,query):
    collection=get_collection(collection_name)
    return collection.find_one(query)
    

#Find multiple documents in collection , collection_name,query (something is there , we need to list it)
def find(collection_name,query):
    collection=get_collection(collection_name)
    if query is None:
        query={}
    return list(collection.find(query))
    

#Update one document in collection, arguements are collection_name,query,update_name
def update_one(collection_name,query,update_value):
    collection=get_collection(collection_name)
    return collection.update_one(query,update_value)
    

#Delete one document from collection,collection_name,query
def delete_one(collection_name,query):
    collection=get_collection(collection_name)
    return collection.delete_one(query)


sample_student = {
    "roll_no": "2026CS101",
    "name": "Rahul Kumar",
    "branch": "CSE",
    "year": 1,
    "email": "rahul.k@iiits.in",
    "subjects": ["C Programming", "Digital Logic", "Math"],
    "is_active": True
}

print(insert_one('students',sample_student))