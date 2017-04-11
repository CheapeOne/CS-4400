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

# These should only be accessible if you have city scientist authorization   

@app.route('/city-scientist')
def city_scientist():
    return render_template('city-scientist.html') 

@app.route('/city-scientist/add-point')
def add_point():
    return render_template('add-point.html')

@app.route('/city-scientist/add-location')
def add_location():
    return render_template('add-location.html')

# These should only be accessible if you have city official authorization

@app.route('/city-official')
def city_official():
    return render_template('city-official.html')   

# These should only be accessible if you have admin authorization

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin/pending-points')
def pending_points():
    return render_template('pending-points.html')

@app.route('/admin/pending-accounts')
def pending_accounts():
    return render_template('pending-accounts.html')
