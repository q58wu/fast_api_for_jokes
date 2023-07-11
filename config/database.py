from pymongo import MongoClient

mongoDBClient = MongoClient("mongodb+srv://robinwu1224:1q2w3e4r@cluster0.njszeok.mongodb.net/?retryWrites=true&w=majority")


db = mongoDBClient.jokes_db

jokesCollection = db["jokes_collection"]
