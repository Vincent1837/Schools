from pymongo import MongoClient
import pprint
client = MongoClient(host="localhost", port=27017)

db = client.Company
for STs in db.Employee.find():
     pprint.pprint(STs)
print("---------------------------------------------------------------------")
for STs in db.Employee.find({"Name": "Brian"}):
     pprint.pprint(STs)
