import pymysql


def connect():
    db = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='cheape42', db='cs4400db')

    cursor = db.cursor()

    return db, cursor


def disconnect(db, cursor):
    cursor.close()
    db.close()


def login_user(username, password):
    db, cursor = connect()

    query = '''SELECT username,password from User where username=%s and password = %s'''
    cursor = db.cursor()
    cursor.execute( query,(self.username,password))
    db.close()

    cursor.execute(query)
    if cursor.execute =='':
     
       return('Login failed',"Check username and password")
       


    disconnect(db, cursor)


def add_user(email, username, password, type):
    db, cursor = connect()
 if user == '':
         return('Error',"Registration Failed: Empty User name")

     if user == '''SELECT username from GTChatUsers where username = user''':
         return('Error',"Registration Failed: Username taken")
         
     if passwd != confirm:
         return('Error',"Registration Failed: Password does not mach confirmation")
         
    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)

def get_pending_officials():
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def unpend_user(username):
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def add_point(type, value, location, date):
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def get_pending_points():
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def add_location(name, zip, city, state):
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)

def get_locations():
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def flag_location(name):
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)


def make_report():
    db, cursor = connect()

    query = "SELECT * FROM User"

    cursor.execute(query)

    print("Results...")

    for row in cursor:
        print(row)

    disconnect(db, cursor)



