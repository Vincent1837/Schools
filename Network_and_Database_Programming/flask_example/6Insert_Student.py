from flask import Flask, request, render_template
import MySQLdb
app = Flask(__name__)

@app.route('/Insert', methods=['GET', 'POST'])
def Insert():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        #  利用request取得表單欄位值
        Name=request.values['StudentName']
        ID=request.values['StudentId']
        Grade=request.values['StudentGrade']
        Sex=request.values['StudentSex']
        # 組成SQL指令
        sqlstatemens="Insert into Student values (" + "\'" + Name + "\'"+ ", " +  ID + ", "+ Grade + ", " +  "\'"+ Sex +  "\'" +")"
        #return sqlstatemens
        # 連結資料庫 
        db=MySQLdb.connect(host="localhost", user="newuser", password="Test1234", db="student_db")
        cur=db.cursor()
        #執行SQL指令
        cur.execute(sqlstatemens)
        cur.execute("Select * from Student" )
        result =cur.fetchall()
        output = str(result) #將tuple轉成String
        db.commit() #Commit指令需要在return之前
        db.close()
        return render_template('Insert.html',messages=output) #將messages帶入HTML檔案中
    #  非POST的時候就會回傳一個空白的模板
    return render_template('Insert.html')


@app.route('/')
def index():
 return 'Hello ' 

if __name__ == '__main__':
    app.debug = True
    app.run()  