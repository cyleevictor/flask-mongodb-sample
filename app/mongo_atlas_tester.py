from pymongo import MongoClient
import datetime

CONNECTION_STRING = "mongodb+srv://victormongo:zM28110b@cluster0.vxluc.mongodb.net/core?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)

db = client.get_database("gettingStarted")
print(f"DB retrieved: {db.name}")

people = db.people
print("collection people created")


personDocument = {
  "name": { "first": "Joe", "last": "Doe" },
  "birth": datetime.datetime(1914, 6, 23),
  "death": datetime.datetime(1955, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}

people.insert_one(personDocument)
