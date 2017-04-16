from app import app
from flask import Flask, url_for, render_template, request, jsonify


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/login/validate', methods=['POST'])
def validate_login():
    print("Logging in a user...")
    username = request.form["username"]

    # TODO: Call method to do SQL stuff...

    return jsonify({"msg": "success"})


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/validate', methods=['POST'])
def validate_registration():
    print("Registering a user...")
    username = request.form["username"]

    # TODO: Call method to do SQL stuff...

    return jsonify({"msg": "success"})

# These should only be accessible if you have city scientist authorization


@app.route('/city-scientist')
def city_scientist():
    return render_template('city-scientist/city-scientist.html')


@app.route('/city-scientist/add-point')
def add_point():
    return render_template('city-scientist/add-point.html')


@app.route('/city-scientist/add-point/validate', methods=['POST'])
def validate_point():
    print("Adding data point")

    # TODO: Call method to do SQL stuff...

    return jsonify({"msg": "success"})


@app.route('/city-scientist/add-location')
def add_location():
    return render_template('city-scientist/add-location.html')


@app.route('/city-scientist/add-location/validate', methods=['POST'])
def validate_location():
    print("Adding poi location")

    # TODO: Call method to do SQL stuff...

    return jsonify({"msg": "success"})

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
