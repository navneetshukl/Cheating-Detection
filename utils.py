import pymongo,database,base64

from pymongo import MongoClient

def Connect_To_DB():

    
    cluster=MongoClient(database.DB_URI)

    db=cluster["Exam"]
   # collection=db["details"]
    return db

