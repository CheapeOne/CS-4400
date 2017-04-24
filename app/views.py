from app import app
from app import model
from pprint import pprint
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        result = model.check_user(username, password)
        if result == None:
            error='Invalid Credentials. Please try again.'
        else:
            user_type = model.get_user_type(username)
            user_type = user_type['User_Type']
            if user_type == 'admin':
                return redirect(url_for("admin", username=username))
            else:
                pend = model.is_official_pending(username)
                if pend['Approved'] == 'pending':
                    error = 'Your account is still pending approval.'
                    return render_template('login.html', error=error)
                if pend['Approved'] == 'rejected':
                    error = 'Your account was rejected approval.'
                    return render_template('login.html', error=error)
                if user_type == 'city official':
                    return redirect(url_for("city_official", username=username))
                if user_type == 'city scientist':
                    return redirect(url_for("city_scientist", username=username))

    return render_template('login.html', error=error)

@app.route('/login/validate', methods=['POST'])

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/validate', methods=['POST'])
def validate_registration():
    print("Registering a user...")

    result = model.add_user(request.form["username"], request.form["email"], request.form["password"], request.form["confirm"], request.form["type"])

    # Regardless of success or failure, keep us on the register page and show a message.
    flash(result[1])
    return jsonify({"destination": '/register'})


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

    result = model.add_location(request.form["poi"], request.form["city"], request.form["state"], request.form["zip"])

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


@app.route('/city-official/poi-search/get-results')
def get_search_results():

    result = model.search_locations(request.args.get('poi', None), request.args.get('city', None), request.args.get('state', None), request.args.get('zipcode', None), request.args.get('flagged', None), request.args.get('flagged-after', None), request.args.get('flagged-before', None))

    return jsonify({"msg": result[1]})


@app.route('/city-official/poi-detail')
def poi_detail():
    return render_template('city-official/poi-detail.html')

@app.route('/city-official/poi-detail/details')
def get_poi_detail():
    result = model.get_poi_detail(request.args.get('type', None), request.args.get('data-greater', None), request.args.get('data-lesser', None), request.args.get('date-after', None), request.args.get('date-before', None))
    return jsonify({"points": result[1]})

@app.route('/city-official/poi-detail/all')
def get_poi_points():
    result = model.get_poi_points(request.args.get('poi'))
    return jsonify({"points": result[1]})

@app.route('/city-official/poi-detail/is-flagged')
def get_is_flagged():
    result = model.get_is_flagged(request.args.get('poi'))
    return jsonify({"flagged": result[1]})

@app.route('/city-official/poi-detail/set-flagged')
def set_is_flagged():
    result = model.set_is_flagged(request.args.get('poi'), request.args.get('flagged'))
    flash(result[1])
    return jsonify({"flagged": result[1]})

@app.route('/city-official/poi-report')
def poi_report():
    return render_template('city-official/poi-report.html')

@app.route('/city-official/poi-report/make')
def make_poi_report():
    result = model.make_report()
    return jsonify({"report": result[1]})



# These should only be accessible if you have admin authorization


@app.route('/admin')
def admin():
    return render_template('admin/admin.html')


@app.route('/admin/pending-points')
def pending_points():
    return render_template('admin/pending-points.html')


@app.route('/admin/pending-points/get')
def get_pending_points():
    result = model.get_pending_points()

    return jsonify({"points": result[1]})


@app.route('/admin/pending-points/accept')
def accept_pending_point():
    poi = request.args.get('poi')
    time = request.args.get('time')

    result = model.set_point_status(poi, time, 'approved')

    flash(result[1])
    return render_template('admin/pending-points.html')


@app.route('/admin/pending-points/reject')
def reject_pending_point():
    poi = request.args.get('poi')
    time = request.args.get('time')

    result = model.set_point_status(poi, time, 'rejected')

    flash(result[1])
    return render_template('admin/pending-points.html')


@app.route('/admin/pending-accounts')
def pending_accounts():
    return render_template('admin/pending-accounts.html')


@app.route('/admin/pending-accounts/get')
def get_pending_accounts():
    result = model.get_pending_officials()

    return jsonify({"accounts": result[1]})


@app.route('/admin/pending-accounts/accept')
def accept_pending_account():
    username = request.args.get('user')

    result = model.set_official_status(username, 'approved')

    flash(result[1])
    return render_template('admin/pending-accounts.html')


@app.route('/admin/pending-accounts/reject')
def reject_pending_account():
    username = request.args.get('user')

    result = model.set_official_status(username, 'rejected')

    flash(result[1])
    return render_template('admin/pending-accounts.html')

@app.route('/city-state/states')
def get_states():

    result = model.get_states()

    return jsonify({"states": result[1]})

@app.route('/city-state/cities')
def get_cities():

    result = model.get_cities()

    return jsonify({"cities": result[1]})

@app.route('/data-type/types')
def get_data_types():

    result = model.get_data_types()

    return jsonify({"types": result[1]})

@app.route('/poi/locations')
def get_all_locations():

    result = model.get_location_names()

    return jsonify({"locations": result[1]})
