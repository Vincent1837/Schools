from pymongo import MongoClient
import pprint
client = MongoClient(host="localhost", port=27017)

db = client.Company
for STs in db.Employee.find():
     pprint.pprint(STs)
print("---------------------------------------------------------------------")
ST1= { "Name": "XXX", "age": 40}
ST2= { "Name": "AAA", "age": 18}
ST3= { "Name": "BBB", "age": 30}
db.Employee.insert_one(ST1)
db.Employee.insert_many([ST2, ST3])
for STs in db.Employee.find():
     pprint.pprint(STs)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
