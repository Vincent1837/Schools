import wx
import MySQLdb  # 使用 MySQLdb 代替 pymysql

# 連接到MySQL數據庫
def connect_db():
    return MySQLdb.connect(
        host='127.0.0.1',  # MySQL服務器地址
        user='root',       # 用戶名
        passwd='ag061837',  # 密碼
        db='test'  # 資料庫名稱
    )
    
db = connect_db()
cur = db.cursor()
cur.execute("DELETE FROM STUDENT WHERE fname = '蔡';")
db.commit()
db.close()