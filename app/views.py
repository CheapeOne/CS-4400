from app import app
from flask import Flask, url_for, render_template
from flask.ext.mysql import MySQL

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login/validate')
def login():
    pass

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register/validate')
def register():
    pass

# These should only be accessible if you have city scientist authorization

@app.route('/city-scientist')
def city_scientist():
    return render_template('city-scientist/city-scientist.html')

@app.route('/city-scientist/add-point')
def add_point():
    return render_template('city-scientist/add-point.html')

@app.route('/city-scientist/add-location')
def add_location():
    return render_template('city-scientist/add-location.html')

# These should only be accessible if you have city official authorization

@app.route('/city-official')
def city_official():
    return render_template('city-official/city-official.html')

@app.route('/city-official/search')
def search():
    return render_template('city-official/search.html')

@app.route('/city-official/poi-report')
def poi_report():
    return render_template('city-official/poi-report.html')

# These should only be accessible if you have admin authorization

@app.route('/admin')
def admin():
    return render_template('admin/admin.html')

@app.route('/admin/pending-points')
def pending_points():
    return render_template('admin/pending-points.html')

@app.route('/admin/pending-accounts')
def pending_accounts():
    return render_template('admin/pending-accounts.html')
