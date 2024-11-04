from flask import Flask, request, render_template
import math
import pymongo

app = Flask(__name__)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")  #連結Mongo資料庫
mydb = myclient["mydatabase"] #連結mydatabase資料庫
mycol = mydb["student"]  #連結student collection

#連線到/write這個路由寫入資料
@app.route("/write",methods=['GET','POST'])
def write():                 #資料寫入資料庫
    mylist = [
              { "studentId": "0401","name": "Amy","subject": "A","score": "100"},
              { "studentId": "0402","name": "Tom","subject": "A","score": "95"},
              { "studentId": "0403","name": "Apple","subject": "B","score": "80"},
              { "studentId": "0404","name": "Peggy","subject": "A","score": "100"},
              { "studentId": "0405","name": "John","subject": "C","score": "85"},
              { "studentId": "0406","name": "Kyle","subject": "A","score": "100"},
              { "studentId": "0407","name": "Sandy","subject": "C","score": "100"},
              { "studentId": "0408","name": "Cindy","subject": "A","score": "98"},
              { "studentId": "0409","name": "Candy","subject": "B","score": "99"},
              { "studentId": "0410","name": "Tommy","subject": "B","score": "87"},
              { "studentId": "0411","name": "Alex","subject": "A","score": "89"},
              { "studentId": "0412","name": "Ava","subject": "C","score": "92"},
              { "studentId": "0413","name": "Carol","subject": "C","score": "97"},
              { "studentId": "0414","name": "Eve","subject": "C","score": "95"},
              { "studentId": "0415","name": "Gene","subject": "B","score": "91"},
              { "studentId": "0416","name": "Judy","subject": "A","score": "100"},
              { "studentId": "0417","name": "Jode","subject": "A","score": "70"},
              { "studentId": "0418","name": "Allen","subject": "B","score": "79"},
              { "studentId": "0419","name": "Ben","subject": "C","score": "94"},
              { "studentId": "0420","name": "Bill","subject": "A","score": "100"},
              ]
    mycol.insert_many(mylist) # 輸入資料
    return("insert data completed")

if __name__ == '__main__':
    app.debug = True
    app.run()