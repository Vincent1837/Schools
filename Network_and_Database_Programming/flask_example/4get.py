from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/getname', methods=['GET'])
def login():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('get.html',user_name=name ,user_email=email)

if __name__ == '__main__':
    app.debug = True
    app.run()  
    