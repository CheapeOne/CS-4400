from app import app
from flask import Flask, url_for, render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    return render_template('index.html', name=name)
