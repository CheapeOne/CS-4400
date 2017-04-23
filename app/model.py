import pymysql


def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         passwd='kimo64', db='cs4400db', cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()

    return db, cursor


def disconnect(db, cursor):
    cursor.close()
    db.close()


def check_user(username, password):
    db, cursor = connect()
    query = "SELECT Username, Password FROM User WHERE Username = '%(username)s' AND Password = '%(password)s'" % locals(
    )
    cursor.execute(query)
    row = cursor.fetchone()
    if username == "":
        return(False, "Login Failed: Empty username field")

    if password == "":
        return(False, "Login Failed: Empty password field")
    sql = "SELECT username from User where  Username = '%(username)s'" % locals(
    )
    if cursor.execute(sql) == '':
        return(False, "Username or Password are wrong")

    disconnect(db, cursor)
    return (True, "yay")


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
    locationtimeexists = "SELECT count(POI_Location_Name) from data_point where POI_Location_Name = '%(location)s' and Date_Time = '%(timeanddate)s'" % locals()
    cursor.execute(locationtimeexists)
    locationtimecount = cursor.fetchall()
    if locationtimecount[0]['count(POI_Location_Name)'] != 0:
        return(False, "This location already exists.")
    if Value == '':
        return(False, 'Please enter value')
    if timeanddate == '':
        return(False, 'Please enter time and date')
    try:
        int(Value)
    except:
        return(False, "Please enter an integer for Data Value.")

    query = "INSERT INTO Data_Point (Data_Type, Data_Value, POI_Location_Name, Date_Time,Accepted) VALUES ('%(Type)s', '%(Value)s', '%(location)s', '%(timeanddate)s','Pending')" % locals()

    cursor.execute(query)
    db.commit()
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


def search_locations(poi, city, state, zipcode, flagged, flagged_after=None, flagged_before=None):


    if poi == '0':
        poi = 'No'
    else:
        poi == 'Yes'

    return (True, "WOAH hey this is not actually working how about that")

    db, cursor = connect()

    query = "SELECT * FROM POI where Location_Name='%(poi)s' AND City = '%(city)s' AND State = '%(state)s' AND,Zip_Code =  '%(zipcode)s' AND Flagged = '%(flagged)s'"%locals()

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
    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def make_report(Type, valueL, valueU, time_dateL, time_dateU):
    db, cursor = connect()

    query = "SELECT * FROM Data_Point where Type = '%(Type)s' UNION SELECT * FROM Data_Point WHERE Data_Value BETWEEN '%(valueL)s' AND '%(valueU)s' UNION SELECT * from Data_Point WHERE time_date BETWEEN '%(time_dateL)s' AND '%(time_dateU)s'" % locals()

    cursor.execute(query)

    data = cursor.fetchall()

    disconnect(db, cursor)

    return (True, data)


def poi_detail(Type, ValueL, ValueU, tdL, tdU):
    db, cursor = connect()

    query = "SELECT * FROM DATA_Point where Data_Type = '%(Type)s' AND Data_Value BETWEEN '%(ValueL)s' AND '%(ValueU)s' AND time_date BETWEEN '%(tdL)s' AND '%(tdU)s'" % locals()

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
