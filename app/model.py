import pymysql


def connect():
    db = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='0ktob3r_902107*', db='cs4400db')

    cursor = db.cursor()

    return db, cursor


def disconnect(db, cursor):
    cursor.close()
    db.close()


def login_user(username, password):
    db, cursor = connect()

    query = "SELECT username, password from User where username = {username} and password = {password}"
    cursor = db.cursor()
    cursor.execute(query)
    db.close()

    cursor.execute(query)
    if cursor.execute =="":

       return("Login failed", "Check username and password")



    disconnect(db, cursor)


def add_user(emailaddress, user, password, confirm, Type):
    db, cursor = connect()
    if user == "":
         return("Error", "Registration Failed: Empty User name")

    if user == "SELECT username from Users where username = user":
         return("Error", "Registration Failed: Username taken")

    if email == "":
         return("Error", "Registration Failed: Empty Email")

    if emailaddress == "SELECT username from Users where email = emailaddress":
         return("Error", "Registration Failed: Email taken")

    if password == "":
         return("Error", "Registration Failed: You must enter a password.")

    if password != confirm:
         return("Error", "Registration Failed: Password does not match confirmation")

    query = "INSERT INTO Users (email, username, password, Type) VALUES ({emailaddress}, {user}, {password}, {Type})"
    cursor.execute(query)
    db.commit()

    disconnect(db, cursor)

    return "done"



def get_pending_officials():
    db, cursor = connect()

    query = "SELECT * FROM City_Official WHERE Approved = pending"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def unpend_user(username,status):
    db, cursor = connect()

    query = "SELECT * from User where username = {username}"

    cursor.execute(query,(username))
    if cursor.execute =="":
        return "Please enter username"
    sql = "UPDATE City Officials set status = {status}"
    cursor.execute(sql,(status))
    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def add_point(location, timeanddate, Type, Value):
    db, cursor = connect()

    if type(Value) != int:
        return("Error: Please enter an integer for Data Value.")

    query = "INSERT INTO Data_Point (Data_Type, Data_Value, POI_Location_Name, DateTime) VALUES ({Type}, {Value}, {location}, {timeanddate})"

    cursor.execute(query)

    disconnect(db, cursor)




def get_pending_points():
    db, cursor = connect()

    query = "SELECT * FROM Data_Point WHERE status = 'pending'"

    cursor.execute(query)

    for row in cursor:
        print(row)

    disconnect(db, cursor)



def add_location(name, city, state, zip):
    db, cursor = connect()

    query = "INSERT INTO POI (Location_Name, Zip_Code, City, State) VALUES ({name}, {zip}, {city}, {state})"

    cursor.execute(query)

    disconnect(db, cursor)




def get_locations():
    db, cursor = connect()

    query = "SELECT * FROM POI"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def flag_location(name,status):
    db, cursor = connect()

    query = "SELECT * FROM POI WHERE Location_Name = {name}"

    cursor.execute(query,(name))
    if cursor.execute == '':
        return "doesnt exist"
    sql = "UPDATE POI set status = status"
    cursor.execute(sql,(status))
    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def make_report(Type,valueL,valueU,time_dateL,time_dateU):
    db, cursor = connect()

    query = "SELECT * FROM Data_Point where Type = Type UNION SELECT * FROM Data_Point WHERE Data_Value BETWEEN valueL AND valueU UNION SELECT * from Data_Point WHERE time_date BETWEEN time_dateL AND time_dateU"


    cursor.execute(query,(Type,valueL,valueU,time_dateL,time_dateU))

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)
