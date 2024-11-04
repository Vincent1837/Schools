from flask import Flask, render_template,request

app = Flask(__name__)

import math
import pymongo

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
    return index()

total = 0 
@app.route("/",methods=['GET','POST'])   #使用http://127.0.0.1:5000/?p=3 URL來列出資料
def index():
    myresult = mycol.find({})    #取出所有學生資料
    total = len(list(mycol.find({}))) # 計算總資料數
    page_card = 5 # 設定一頁顯示幾筆資料
    page_total = int(math.ceil(total/page_card)) # 計算需要幾頁
    p = request.args.get('p') # 取得當前頁次 
    show_status = 0

    if not p:
        p = 1
    else:
        p = int(p)
        if p > 1:
            show_status = 1
    start = (p-1)*page_card # 個別頁面從哪筆資料開始顯示
    show = myresult.skip(start).limit(page_card) # 此頁面要展示的資料的list，從start開始page_card筆資料
    page_list =range(1, 10) #先顯示頁碼1-9，動態頁碼使用以下age_list = get_page(page_total, p)
    #page_list = get_page(page_total, p) # 頁碼要顯示多少到多少的list
    datas = {       # tuple有目前頁碼， 總共頁數，要顯示在底下的頁碼list, 是否顯示
        'p' : p,
        'page_total' : page_total,
        'page_list' : page_list,
        'show_status' : show_status,
    }
    return render_template("flask_and_mongodb.html",show = show, pdatas=datas)

def get_page(total,p):
    show_page = 5 # 一次顯示幾個頁碼
    pageoffset = 2 # 頁碼的偏移量
    start = 1 # 從頁碼1開始
    end = total 
    
    if total > show_page:
        if p > pageoffset:
            start = p - pageoffset
            if total > p + pageoffset:
                end = p + pageoffset
            else:
                end = total
        else:
            start = 1
            if total > show_page:
                end = show_page
            else:
                end = total
        if p + pageoffset > total:
            start = start - (p + pageoffset - end)

    dic = range(start, end + 1) # 要顯示那些頁碼
    return dic

if __name__ == '__main__':
    app.debug = True
    app.run()