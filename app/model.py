import pymysql
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash

def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         passwd='0ktob3r_902107*', db='cs4400db', cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()
    return db, cursor


def disconnect(db, cursor):
    cursor.close()
    db.close()


def check_user(username, password):
    db, cursor = connect()

    query = "SELECT Username, Password FROM User WHERE Username = '%(username)s' AND Password = '%(password)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()

    disconnect(db, cursor)

    return row;


def get_user_type(username):
    db, cursor = connect()

    query = "SELECT User_Type FROM User WHERE Username = '%(username)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()

    disconnect(db, cursor)

    return row;


def is_official_pending(username):
    db, cursor = connect()

    query = "SELECT Approved FROM City_Official WHERE Username = '%(username)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()

    disconnect(db, cursor)

    return row;


def add_user(emailaddress, user, password, confirm, Type):
    db, cursor = connect()
    if user == "":
        return(False, "Registration Failed: Empty User name")

    if user == "SELECT username from Users where username = user":
        return(False, "Registration Failed: Username taken")

    if emailaddress == "":
        return(False, "Registration Failed: Empty Email")

    if emailaddress == "SELECT username from Users where email = emailaddress":
        return(False, "Registration Failed: Email taken")

    if password == "":
        return(False, "Registration Failed: You must enter a password.")

    if password != confirm:
        return(False, "Registration Failed: Password does not match confirmation")

    query = "INSERT INTO User (Email, Username, Password, User_Type) VALUES ('%(emailaddress)s', '%(user)s', '%(password)s', '%(Type)s')" % locals()

    cursor.execute(query)
    db.commit()

    disconnect(db, cursor)

    return (True, "Registration Successful!")


def get_pending_officials():
    db, cursor = connect()

    query = "SELECT o.Username, o.Title, o.City, o.State, o.Approved, u.Email FROM City_Official o JOIN User u ON o.Username = u.Username WHERE o.Approved = 'pending'"

    cursor.execute(query)

    data = cursor.fetchall()

    disconnect(db, cursor)
    return (True, data)


def set_official_status(username, status):
    db, cursor = connect()

    print(username, status)

    sql = "UPDATE City_Official SET Approved = '%(status)s' WHERE username = '%(username)s'" % locals(
    )
    print(sql)
    cursor.execute(sql)
    db.commit()

    disconnect(db, cursor)

    return (True, "Account status updated!")


def set_point_status(poi, time, status):
    db, cursor = connect()

    sql = "UPDATE Data_Point SET Accepted = '%(status)s', Date_Time = Date_Time WHERE POI_Location_Name = '%(poi)s' AND Date_Time = '%(time)s'" % locals()

    cursor.execute(sql)
    db.commit()
    disconnect(db, cursor)
    return(True, "Point status updated!")


def add_point(location, timeanddate, Type, Value):
    db, cursor = connect()
    if Value == '':
        return(False, 'Please enter value')
    if timeanddate == '':
        return(False, 'Please enter time and date')
    try:
        int(Value)
    except:
        return(False, "Please enter an integer for Data Value.")

    query = "INSERT INTO Data_Point (Data_Type, Data_Value, POI_Location_Name, Date_Time) VALUES ('%(Type)s', '%(Value)s', '%(location)s', '%(timeanddate)s')" % locals()

    cursor.execute(query)

    disconnect(db, cursor)

    return (True, "Point added!")


def get_pending_points():
    db, cursor = connect()

    query = "SELECT * FROM Data_Point WHERE Accepted = 'pending'"

    cursor.execute(query)

    data = cursor.fetchall()

    disconnect(db, cursor)

    return (True, data)


def add_location(poilocation, city, state, zip):
    db, cursor = connect()
    locationexists = "SELECT count(Location_Name) from poi where Location_Name = '%(poilocation)s'" % locals()
    cursor.execute(locationexists)
    locationcount = cursor.fetchall()
    if locationcount[0]['count(Location_Name)'] != 0:
        return(False, "This location already exists.")
    elif len(zip) != 5:
        return(False, "Please enter a valid zip code.")
    else:
        try:
            query = "INSERT INTO POI (Location_Name, Zip_Code, City, State) VALUES ('%(poilocation)s', %(zip)s, '%(city)s', '%(state)s')" % locals()
            cursor.execute(query)
        except:
            return(False, "This location does not exist.")
        db.commit()
        disconnect(db, cursor)

        return (True, "Location Added!")



def search_locations(poi=None, city=None, state=None, zipcode=None, flagged=None, flagged_after=None, flagged_before=None):
    if poi == 'No':
        poi = '0'
    else:
        poi == '1'
    db, cursor = connect()

    namef = (poi if "WHERE Location_Name = '%(poi)s'" else " ") % locals()
    cityf = (city if "WHERE City = '%(city)s'" else " ") % locals()
    statef = (state if "WHERE State = '%(state)s'" else " ") % locals()
    zipf = (zipcode if "WHERE Zip_Code = '%(zipcode)s'" else " ") % locals()
    flaggedf = (flagged if "WHERE Flagged = '%(flagged)s'" else " ") % locals()
    flaggedafterf = (flagged_after if "WHERE Date_Flagged < '%(flagged_after)s'" else " ") % locals()
    flaggedbeforef = (city if "WHERE Date_Flagged > '%(flagged_before)s'" else " ") % locals()

    query = "SELECT * FROM POI" + namef + cityf + statef + zipf + flaggedf + flaggedafterf + flaggedbefore

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def flag_location(name, status):
    db, cursor = connect()

    query = "SELECT * FROM POI WHERE Location_Name='%(name)s'" % locals()
    cursor.execute(query)
    if cursor.execute == "":
        return (False, "doesnt exist")
    sql = "UPDATE POI set Flagged = '%(status)s'" % locals()
    cursor.execute(sql)
    
    db.commit()

    disconnect(db, cursor)


def make_report():
    db, cursor = connect()

    query = "SELECT * from (select POI_Location_Name, City, State, min(Data_Value) as min_value_mold, AVG(Data_Value) as avg_value_mold, MAX(Data_Value) as max_value_mold, COUNT(Data_Value) as count_mold, Flagged from data_point join poi on data_point.POI_Location_Name = poi.Location_Name WHERE Data_Type = 'Air Quality' GROUP BY POI_Location_Name) as A natural join (select POI_Location_Name, City, State, min(Data_Value) as min_value_airquality, AVG(Data_Value) as avg_value_airquality, MAX(Data_Value) as max_value_airquality, COUNT(Data_Value) as count_airquality, Flagged from data_point join poi on data_point.POI_Location_Name = poi.Location_Name WHERE Data_Type = 'Air Quality' GROUP BY POI_Location_Name) as B"

    cursor.execute(query)
    data = cursor.fetchall()

    disconnect(db, cursor)

    return (True, data)


def get_poi_details(Type=None, ValueL=None, ValueU=None, tdL=None, tdU=None):
    db, cursor = connect()

    query = "SELECT * FROM Data_Point where Data_Type = '%(Type)s' AND Data_Value BETWEEN '%(ValueL)s' AND '%(ValueU)s' AND time_date BETWEEN '%(tdL)s' AND '%(tdU)s'" % locals()

    cursor.execute(query)

    data = cursor.fetchall()

    disconnect(db, cursor)

    return (True, data)

def get_is_flagged(poi=None):
    db, cursor = connect()

    query = "SELECT Flagged FROM POI where Location_Name = '%(poi)s'" % locals()

    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(db, cursor)

    return (True, data)

def set_is_flagged(poi=None, flagged=None):
    db, cursor = connect()

    query = "UPDATE POI set Flagged = '%(flagged)s'" % locals()

    cursor.execute(query)
    db.commit()
    disconnect(db, cursor)

    return (True, "Set POI flag!")


def get_poi_points(poi):
    db, cursor = connect()
    query = "SELECT * FROM Data_Point where POI_Location_Name = '%(poi)s'" % locals()
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(db, cursor)

    return (True, data)

def get_states():
    db, cursor = connect()
    query = "SELECT DISTINCT State FROM City_State"
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(db, cursor)
    return (True, data)


def get_cities():
    db, cursor = connect()
    query = "SELECT DISTINCT City FROM City_State"
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(db, cursor)
    return (True, data)

def get_data_types():
    db, cursor = connect()
    query = "SELECT DISTINCT Type FROM Data_Type"
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(db, cursor)
    return (True, data)


def get_location_names():
    db, cursor = connect()
    query = "SELECT DISTINCT Location_Name FROM POI"
    cursor.execute(query)
    data = cursor.fetchall()
    disconnect(db, cursor)
    return (True, data)
