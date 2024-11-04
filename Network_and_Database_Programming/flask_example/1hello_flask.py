from flask import Flask
from flask import url_for,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello flask'

@app.route('/user/<username>')
def username(username):
    return 'i am ' + username

@app.route('/age/<int:age>')
def userage(age):
    return 'i am ' + str(age) + ' years old'

@app.route('/a')
def url_a():
    return 'here is a'

@app.route('/b')
def b():
    #  所得結果為'/a'
    return url_for('url_a')

@app.route('/c')
def c():
    #  會將使用者引導到'/a'這個路由
    return redirect(url_for('url_a'))

if __name__ == '__main__':
    app.debug = True
    app.run()