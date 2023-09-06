import pymongo,database

from pymongo import MongoClient

def Connect_To_DB():

    
    cluster=MongoClient(database.DB_URI)

    db=cluster["Exam"]
   # collection=db["details"]
    return db


"""db=utils.Connect_To_DB()
    collection=db["user"]
    post={"name":"Ram","email":"ram.com","password":"Ayodhya"}

    collection.insert_one(post)
    return JsonResponse({'Message': "Connected to Database"})
"""