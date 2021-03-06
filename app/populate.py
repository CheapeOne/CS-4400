import pymysql
import random as rand
import sys
import time

db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     passwd="Elite12$",
                     db="cs4400db"
                     )

cur = db.cursor()

city_states_list = {
    "New York": "New York",
    "Los Angeles": "California",
    "Chicago": "Illinois",
    "Houston": "Texas",
    "Philadelphia": "Pennsylvania",
    "Phoenix": "Arizona",
    "San Antonio": "Texas",
    "San Diego": "California",
    "Dallas": "Texas",
    "San Jose": "California",
    "Austin": "Texas",
    "Jacksonville": "Florida",
    "San Francisco": "California",
    "Indianapolis": "Indiana",
    "Columbus": "Ohio",
    "Fort Worth": "Texas",
    "Charlotte": "North Carolina",
    "Seattle": "Washington",
    "Denver": "Colorado",
    "El Paso": "Texas",
    "Atlanta": "Georgia",
}

data_types = ["Mold", "Air Quality"]

random_locations = [
    # Name, City, State, Zip Code
    ("Georgia Tech", "Atlanta", "Georgia", "30332"),
    ("Centennial Olympic Park", "Atlanta", "Georgia", "30313"),
    ("Emory University", "Atlanta", "Georgia", "30322"),
    ("Times Square", "New York", "New York", "10036"),
    ("Buckingham Fountain", "Chicago", "Illinois", "60605"),
    ("Uchicago", "Chicago", "Illinois", "60637"),
    ("William Street Park", "San Jose", "California", "95112")
]

random_datetimes = [
    # YYYY-MM-DD HH:MM:SS
    "2011-01-01 01:00:00",
    "2011-02-02 12:30:00",
    "2012-03-03 03:00:00",
    "2012-04-04 14:30:00",
    "2013-05-05 05:00:00",
    "2013-06-06 16:30:00",
    "2014-07-07 07:00:00",
    "2014-08-08 18:30:00",
    "2015-09-09 09:00:00",
    "2015-10-10 20:30:00",
    "2016-11-11 11:00:00",
    "2016-12-12 22:30:00"
]

random_dates = [
    # YYYY-MM-DD
    "2011-01-01",
    "2011-02-02",
    "2012-03-03",
    "2012-04-04",
    "2013-05-05",
    "2013-06-06",
    "2014-07-07",
    "2014-08-08",
    "2015-09-09",
    "2015-10-10",
    "2016-11-11",
    "2016-12-12"
]

# Data Types

try:
    cur.execute("INSERT INTO Data_Type VALUES ('Mold'), ('Air Quality')")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print ("\nThe following query failed:")
    print("Error: {0}".format(e))

# CityStates

for city in city_states_list:
    city_state = city_states_list[city]
    insert = "INSERT into City_State VALUES ('%(city)s', '%(city_state)s')" % locals(
    )
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# Admins
try:
    cur.execute(
        "INSERT into User VALUES ('admin0@example\.com', 'admin', 'admin', 'admin')")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print ("\nThe following query failed:")
    print ("INSERT into User VALUES ('admin0@example\.com', 'admin', 'admin', 'admin')")
    print("Error: {0}".format(e))

for num in range(1, 5):
    insert = "INSERT into User VALUES ('admin%(num)s@example\.com', 'admin%(num)s', 'admin%(num)s', 'admin')" % locals(
    )
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# City Scientists

for num in range(10):
    insert = "INSERT into User VALUES ('scientist%(num)s@example\.com', 'scientist%(num)s', 'scientist%(num)s', 'city scientist')" % locals(
    )
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# City Officials

for num in range(10):
    insert = "INSERT into User VALUES ('official%(num)s@example.com', 'official%(num)s', 'official%(num)s', 'city official')" % locals(
    )
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print("\nThe following query failed:")
        print(insert)
        print("Error: {0}".format(e))

for num in range(0, 3):
    city = rand.choice(list(city_states_list))
    state = city_states_list[city]
    insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = 'official%(num)s'), 'Head of Parks and Rec', '%(city)s', '%(state)s', 'pending')" % locals(
    )
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

for num in range(3, 6):
    city = rand.choice(list(city_states_list))
    state = city_states_list[city]
    insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = 'official%(num)s'), 'Head of Sanitation', '%(city)s', '%(state)s', 'rejected')" % locals(
    )
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

for num in range(6, 10):
    city = rand.choice(list(city_states_list))
    state = city_states_list[city]
    insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = 'official%(num)s'), 'City Manager', (SELECT City FROM City_State WHERE City = '%(city)s'), (SELECT DISTINCT State FROM City_State WHERE State = '%(state)s'), 'approved')" % locals()
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# POI Locations

try:
    cur.execute("INSERT INTO POI VALUES ('Georgia Tech', (SELECT DISTINCT City FROM City_State WHERE City = 'Atlanta'), (SELECT DISTINCT State FROM City_State WHERE State = 'Georgia'), '30332', 1, '2017-02-23')")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print("Error: {0}".format(e))

try:
    cur.execute("INSERT INTO POI VALUES ('GSU', (SELECT DISTINCT City FROM City_State WHERE City = 'Atlanta'), (SELECT DISTINCT State FROM City_State WHERE State = 'Georgia'), '30303', 0, NULL)")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print("Error: {0}".format(e))

try:
    cur.execute("INSERT INTO POI VALUES ('Emory University', (SELECT DISTINCT City FROM City_State WHERE City = 'Atlanta'), (SELECT DISTINCT State FROM City_State WHERE State = 'Georgia'), '30322', 0, NULL)")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print("Error: {0}".format(e))

try:
    cur.execute("INSERT INTO POI VALUES ('Uchicago', (SELECT DISTINCT City FROM City_State WHERE City = 'Chicago'), (SELECT DISTINCT State FROM City_State WHERE State = 'Illinois'), '60637', 1, '2017-02-24')")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print("Error: {0}".format(e))

for loc in random_locations:
    insert = "INSERT into POI VALUES ('%s', (SELECT DISTINCT City FROM City_State WHERE City = '%s'), (SELECT DISTINCT State FROM City_State WHERE State = '%s'), '%s', 0, NULL)" % (loc[0], loc[1], loc[2], loc[3])
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))


# Data Points

try:
    cur.execute("INSERT into Data_Point VALUES ((SELECT Location_Name FROM POI WHERE Location_Name = \"Georgia Tech\"), '2017-01-31 15:32', 12, (SELECT Type from Data_Type WHERE Type = 'Mold'), \"approved\")")
    cur.execute("INSERT into Data_Point VALUES ((SELECT Location_Name FROM POI WHERE Location_Name = \"Georgia Tech\"), '2017-02-15 16:12', 42, (SELECT Type from Data_Type WHERE Type = 'Mold'), \"approved\")")
    cur.execute("INSERT into Data_Point VALUES ((SELECT Location_Name FROM POI WHERE Location_Name = \"Georgia Tech\"), '2017-02-24 4:29', 4, (SELECT Type from Data_Type WHERE Type = 'Air Quality'), \"approved\")")
    cur.execute("INSERT into Data_Point VALUES ((SELECT Location_Name FROM POI WHERE Location_Name = \"Georgia Tech\"), '2017-02-01 3:57', 34, (SELECT Type from Data_Type WHERE Type = 'Air Quality'), \"approved\")")
except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
    print("Error: {0}".format(e))

for num in range(10):
    random_time = rand.choice(random_datetimes)
    random_value = rand.randint(1, 100)
    random_type = rand.choice(data_types)
    insert = "INSERT into Data_Point VALUES ((SELECT Location_Name FROM POI WHERE Location_Name = \"Georgia Tech\"), '%(random_time)s', '%(random_value)s', (SELECT Type from Data_Type WHERE Type = '%(random_type)s'), \"pending\")" % locals()
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

for num in range(40):
    random_time = rand.choice(random_datetimes)
    random_value = rand.randint(1, 100)
    random_type = rand.choice(data_types)
    random_location = rand.choice(random_locations)
    random_location_name = random_location[0]
    insert = "INSERT into Data_Point VALUES ((SELECT Location_Name FROM POI WHERE Location_Name = '%(random_location_name)s'), '%(random_time)s', '%(random_value)s', (SELECT Type from Data_Type WHERE Type = '%(random_type)s'), \"pending\")" % locals()
    try:
        cur.execute(insert)
    except (pymysql.err.DataError, pymysql.err.IntegrityError, pymysql.err.InternalError) as e:
        print ("\nThe following query failed:")
        print (insert)
        print("Error: {0}".format(e))

db.commit()
db.close()
