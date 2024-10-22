from pymongo import MongoClient
import pprint
client = MongoClient(host="localhost", port=27017)

db = client.Company
for STs in db.Employee.find():
     pprint.pprint(STs)
print("---------------------------------------------------------------------")

db.Employee.update_one({ 'Name': 'XXX' }, { '$set': { 'age': 100 } } );
db.Employee.update_many({ 'Name': 'Josh' }, { '$set': { 'age': 100 } });


for STs in db.Employee.find():
     pprint.pprint(STs)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
