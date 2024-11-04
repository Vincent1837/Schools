from flask import Flask, request, jsonify, render_template
import pymongo
from pymongo import ASCENDING
import os

# MongoDB 連線設置
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['school']
student_collection = db['students']
course_collection = db['courses']
enrollment_collection = db['enrollments']

# 設定 primary key
student_collection.create_index("sid", unique=True)
course_collection.create_index("cid", unique=True)
enrollment_collection.create_index([("sid", ASCENDING), ("cid", ASCENDING)], unique=True)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        sid = request.form['sid']
        fname = request.form['fname']
        lname = request.form['lname']
        grade = request.form['grade']
        sex = request.form['sex']

        student_data = {
            "sid": sid,
            "fname": fname,
            "lname": lname,
            "grade": grade,
            "sex": sex
        }
        student_collection.insert_one(student_data)
        return jsonify({"message": f"學生 {fname} {lname} 已新增"})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_course', methods=['POST'])
def add_course():
    try:
        cid = request.form['cid']
        cname = request.form['cname']

        course_data = {
            "cid": cid,
            "cname": cname
        }
        course_collection.insert_one(course_data)
        return jsonify({"message": f"課程 {cname} 已新增"})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_enrollment', methods=['POST'])
def add_enrollment():
    try:
        sid = request.form['sid']
        cid = request.form['cid']
        enrollment_data = {
            "sid": sid,
            "cid": cid,
            "midScore": 0,
            "finalScore": 0
        }
        enrollment_collection.insert_one(enrollment_data)
        return jsonify({"message": "選課資料已新增"})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/add_scores', methods=['POST'])
def add_scores():
    try:
        sid = request.form['sid']
        cid = request.form['cid']
        mid = float(request.form['midScore'])
        final = float(request.form['finalScore'])

        enrollment_collection.update_one(
            {
                "$and": [{"sid": sid}, {"cid": cid}]
            },
            {
                "$set": {"midScore": mid, "finalScore": final}
            }
        )
        return jsonify({"message": "期中與期末成績已新增"})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/query_scores', methods=['GET'])
def query_scores():
    try:
        cid = request.args.get('cid')
        enrollments = enrollment_collection.find({"cid": cid})

        student_data = []
        for enrollment in enrollments:
            sid = enrollment["sid"]
            student = student_collection.find_one({"sid": sid})
            mid = enrollment["midScore"]
            final = enrollment["finalScore"]
            total = 0.4 * mid + 0.6 * final

            student_info = {
                'sid': student['sid'],
                'fname': student['fname'],
                'lname': student['lname'],
                'mid': mid,
                'final': final,
                'total': total
            }
            student_data.append(student_info)

        return jsonify(student_data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
