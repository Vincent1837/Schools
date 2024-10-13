import MySQLdb

db = MySQLdb.Connection(host='127.0.0.1', user='root', port=3306, db='test', password='ag061837')

cur = db.cursor()
cur.execute("Select * from employee")

cur.execute("Insert into employee values (55688, 'KoPinYi', 3000000)")

for emp in cur.fetchall():
    print(emp)
    
db.commit()
db.close()