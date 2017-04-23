import pymysql
import random as rand
import sys

db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     passwd="cheape42",
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

random_locations = [
    # Name, City, State, Zip Code
    ("Georgia Tech", "Atlanta", "Georgia", "30332"),
    ("Centennial Olympic Park", "Atlanta", "Georgia", "30313"),
    ("Emory University", "Atlanta", "Georgia", "30322"),
    ("Times Square", "New York", "New York", "10036"),
    ("Buckingham Fountain", "Chicago", "Illinois", "60605"),
    ("William Street Park", "San Jose", "California", "95112")
]

random_datetimes_list = [
    # YYYYMMDD HH:MM:SS
    "20110101 01:00:00 AM",
    "20110202 02:30:00 PM",
    "20120303 03:00:00 AM",
    "20120404 04:30:00 PM",
    "20130505 05:00:00 AM",
    "20130606 06:30:00 PM",
    "20140707 07:00:00 AM",
    "20140808 08:30:00 PM",
    "20150909 09:00:00 AM",
    "20151010 10:30:00 PM",
    "20161111 11:00:00 AM",
    "20161212 12:30:00 PM"
]

# CityStates

for city in city_states_list:
    city_state = city_states_list[city]
    insert = "INSERT into City_State VALUES ('%(city)s', '%(city_state)s')" % locals()
    print(insert)
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print ("The following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# Admins
try:
    cur.execute("INSERT into User VALUES ('admin0@example\.com', 'admin', 'admin', 'admin')")
except pymysql.err.DataError as e:
        print ("The following query failed:")
        print ("INSERT into User VALUES ('admin0@example\.com', 'admin', 'admin', 'admin')")
        print("Error: {0}".format(e))

for num in range(1, 5):
    insert = "INSERT into User VALUES ('admin%(num)s@example\.com', 'admin%(num)s', 'admin%(num)s', 'admin')" % locals()
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print ("The following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# City Scientists

for num in range(10):
    insert = "INSERT into User VALUES ('scientist%(num)s@example\.com', 'scientist%(num)s', 'scientist%(num)s', 'city scientist')" % locals()
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print ("The following query failed:")
        print (insert)
        print("Error: {0}".format(e))

# City Officials

for num in range(10):
    insert = "INSERT into User VALUES ('official%(num)s@example.com', 'official%(num)s', 'official%(num)s', 'city official')" % locals()
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print("The following query failed:")
        print(insert)
        print("Error: {0}".format(e))

for num in range(0, 3):
    city = rand.choice(list(city_states_list))
    state = city_states_list[city]
    insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = 'official%(num)s'), '%(city)s', '%(state)s', 'pending')" % locals()
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print ("The following query failed:")
        print (insert)
        print("Error: {0}".format(e))

for num in range(3, 6):
    city = rand.choice(list(city_states_list))
    state = city_states_list[city]
    insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = 'official%(num)s'), '%(city)s', '%(state)s', 'rejected')" % locals()
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print ("The following query failed:")
        print (insert)
        print("Error: {0}".format(e))

for num in range(6, 10):
    city = rand.choice(list(city_states_list))
    state = city_states_list[city]
    insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = 'official%(num)s'), '%(city)s', '%(state)s', 'approved')" % locals()
    try:
        cur.execute(insert)
    except pymysql.err.DataError as e:
        print ("The following query failed:")
        print (insert)
        print("Error: {0}".format(e))


# POI Locations

# cur.execute("INSERT into POI_Location VALUES ('Georgia Tech', 'Atlanta', 'Georgia', '30332', 'Yes', '02/23/2017')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('GSU', 'Atlanta', 'Georgia', '30303' 'No', '')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('Emory', 'Atlanta', 'Georgia', '30322', 'No', '')")
# cur.execute("INSERT into POI_Location VALUES ('Uchicago', 'Chicago', 'Illinois', '60637', 'Yes', '02/24/2017')")

# # TODO: 6 POI locations

# cur.execute(
#     "INSERT into POI_Location VALUES ('', '', '', '', 'No', '')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('', '', '', '', 'No', '')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('', '', '', '', 'No', '')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('', '', '', '', 'No', '')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('', '', '', '', 'No', '')")
# cur.execute(
#     "INSERT into POI_Location VALUES ('', '', '', '', 'No', '')")

# Data Points
# try:
#     cur.execute(
#         "INSERT into Data_Points VALUES ('Georgia Tech', '01/31/2017 15:32', '12', 'Mold', 'approved')")
#     cur.execute(
#         "INSERT into Data_Points VALUES ('Georgia Tech', '02/15/2017 16:12', '42', 'Mold', 'approved')")
#     cur.execute(
#         "INSERT into Data_Points VALUES ('Georgia Tech', '02/24/2017 4:29', '4', 'Air Quality', 'approved')")
#     cur.execute(
#         "INSERT into Data_Points VALUES ('Georgia Tech', '02/01/2017 3:57', '34', 'Air Quality', 'approved')")
# except pymysql.err.DataError as e:
#     print("Error: {0}".format(e))

# random_value = rand.randint(100)

# try:
#     for num in range(9):
#         insert = "INSERT into Data_Points VALUES ('Georgia Tech', '01/31/2017 15:32', '%s', 'Mold', 'approved')" % (rand.randint(100))
#         cur.execute(insert)
# except pymysql.err.DataError as e:
#     print ("The following query failed:")
#     print (insert)
#     print("Error: {0}".format(e))

# TODO: 36 data points

db.commit()
db.close()
