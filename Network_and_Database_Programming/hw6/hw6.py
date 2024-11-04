from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# MySQL connection
conn = MySQLdb.connect(host='localhost', user='root', password='08220822', db='test')
cursor = conn.cursor()

# Create tables (if they don't exist already)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT (
        SID VARCHAR(10) PRIMARY KEY,
        Fname VARCHAR(100),
        Lname VARCHAR(100),
        Grade INT,
        Sex VARCHAR(10),
        Email VARCHAR(100)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS COURSE (
        CID VARCHAR(10) PRIMARY KEY,
        Cname VARCHAR(100)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ENROLLMENT (
        SID VARCHAR(10),
        CID VARCHAR(10),
        MidScore INT DEFAULT 0,
        FinalScore INT DEFAULT 0,
        PRIMARY KEY (SID, CID),
        FOREIGN KEY (SID) REFERENCES STUDENT(SID),
        FOREIGN KEY (CID) REFERENCES COURSE(CID)
    );
''')
conn.commit()

# Routes and functionalities

@app.route('/')
def home():
    return render_template('home.html')

# A. Add Student Data
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        sid = request.form['sid']
        fname = request.form['fname']
        lname = request.form['lname']
        grade = request.form['grade']
        sex = request.form['sex']
        email = request.form['email']
        
        cursor.execute("INSERT INTO STUDENT (SID, Fname, Lname, Grade, Sex, Email) VALUES (%s, %s, %s, %s, %s, %s)",
                       (sid, fname, lname, grade, sex, email))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('add_student.html')

# B. Add Course Data
@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        cid = request.form['cid']
        cname = request.form['cname']
        
        cursor.execute("INSERT INTO COURSE (CID, Cname) VALUES (%s, %s)", (cid, cname))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('add_course.html')

# C. Add Enrollment Data
@app.route('/add_enrollment', methods=['GET', 'POST'])
def add_enrollment():
    if request.method == 'POST':
        sid = request.form['sid']
        cid = request.form['cid']
        
        cursor.execute("INSERT INTO ENROLLMENT (SID, CID) VALUES (%s, %s)", (sid, cid))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('add_enrollment.html')

# D. Enter Midterm and Final Scores
@app.route('/enter_scores', methods=['GET', 'POST'])
def enter_scores():
    if request.method == 'POST':
        sid = request.form['sid']
        cid = request.form['cid']
        midscore = request.form['midscore']
        finalscore = request.form['finalscore']
        
        cursor.execute("UPDATE ENROLLMENT SET MidScore = %s, FinalScore = %s WHERE SID = %s AND CID = %s",
                       (midscore, finalscore, sid, cid))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('enter_scores.html')

# E. Query Total Scores
@app.route('/query_scores', methods=['GET', 'POST'])
def query_scores():
    if request.method == 'POST':
        cid = request.form['cid']
        cursor.execute('''
            SELECT STUDENT.SID, STUDENT.Fname, STUDENT.Lname, 
                   (0.4 * ENROLLMENT.MidScore + 0.6 * ENROLLMENT.FinalScore) AS TotalScore 
            FROM ENROLLMENT
            JOIN STUDENT ON ENROLLMENT.SID = STUDENT.SID
            WHERE ENROLLMENT.CID = %s
        ''', (cid,))
        results = cursor.fetchall()
        return render_template('query_scores.html', results=results)
    return render_template('query_scores.html')

if __name__ == '__main__':
    app.run(debug=True)
