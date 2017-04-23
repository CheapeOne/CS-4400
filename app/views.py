from app import app
from app import model
import flask
from flask import Flask, url_for, render_template, request, jsonify, flash


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/login/validate', methods=['POST'])
def validate_login():
    print("Logging in a user...")

    result = model.login_user(request.form["username"], request.form["password"])

    if result[0]:
        pass
        # TODO: go to the appropriate login page for the person.
    else:
        # If it failed, keep us on the login page, and flask an error message
        flash(result[1])
        return jsonify({"destination": url_for('login')})


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/validate', methods=['POST'])
def validate_registration():
    print("Registering a user...")

    result = model.add_user(request.form["username"], request.form["email"], request.form["password"], request.form["confirm"], request.form["type"])

    # Regardless of success or failure, keep us on the register page and show a message.
    flash(result[1])
    return jsonify({"destination": url_for('register')})


# These should only be accessible if you have city scientist authorization


@app.route('/city-scientist')
def city_scientist():
    return render_template('city-scientist/city-scientist.html')


@app.route('/city-scientist/add-point')
def add_point():
    return render_template('city-scientist/add-point.html')


@app.route('/city-scientist/add-point/validate', methods=['POST'])
def validate_point():
    print("Adding data point...")

    result = model.add_point(request.form["poi"], request.form["time"], request.form["type"], request.form["value"])

    # Regardless of success or failure, keep us on the add point page and show a message.
    flash(result[1])
    return jsonify({"destination": url_for('add_point')})


@app.route('/city-scientist/add-location')
def add_location():
    return render_template('city-scientist/add-location.html')


@app.route('/city-scientist/add-location/validate', methods=['POST'])
def validate_location():
    print("Adding poi location")

    result = model.add_location(request.form["name"], request.form["city"], request.form["state"], request.form["zip"])

    # Regardless of success or failure, keep us on the add location page and show a message.
    flash(result[1])
    return jsonify({"destination": url_for('add_location')})

# These should only be accessible if you have city official authorization


@app.route('/city-official')
def city_official():
    return render_template('city-official/city-official.html')


@app.route('/city-official/poi-search')
def search():
    return render_template('city-official/search.html')


@app.route('/city-official/poi-search/get-results', methods=['GET'])
def get_search_results():
    print("hey")
    result = model.get_locations()

    return jsonify({"msg": result[1]})


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
