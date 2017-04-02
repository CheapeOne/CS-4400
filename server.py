from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/login')
def login():
    return 'Log In Page'

@app.route('/style')
def style():
    thing = url_for('static', filename='style.css')
    return thing

@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    return render_template('index.html', name=name)





