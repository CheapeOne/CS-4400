import pymysql
import random as rand

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
    ("Georgia Tech", "Atlanta", "Georgia", "30332"),
    ("Centennial Olympic Park", "Atlanta", "Georgia", "30313"),
    ("Emory University", "Atlanta", "Georgia", "30322"),
    ("Times Square", "New York", "New York", "10036"),
    ("Buckingham Fountain", "Chicago", "Illinois", "60605"),
    ("William Street Park", "San Jose", "California", "95112")
]

random_datetimes_list = [
    "20120618 10:34:09 AM"
]

# CityStates

for city in city_states_list:
    city_state = city_states_list[city]
    insert = "INSERT into City_State VALUES ('%(city)s', '%(city_state)s')" % locals()
    print(insert)
    try:
        cur.execute(insert)
    except pymysql.ProgrammingError:
        print ("The following query failed:")
        print (insert)

# # Admins

# cur.execute(
#     "INSERT into User VALUES (\"admin0@example\.com\", \"admin\", \"admin\", \"admin\")")

# for num in range(1, 5):
#     insert = "INSERT into User VALUES (\"admin{num}@example\.com\", \"admin{num}\", \"admin{num}\", \"admin\")"
#     try:
#         cur.execute(insert)
#     except pymysql.ProgrammingError:
#         print ("The following query failed:")
#         print (insert)

# # City Scientists

# for num in range(10):
#     insert = "INSERT into User VALUES (\"scientist{num}@example\.com\", \"scientist{num}\", \"scientist{num}\", \"city scientist\")"
#     try:
#         cur.execute(insert)
#     except pymysql.ProgrammingError:
#         print ("The following query failed:")
#         print (insert)

# # City Officials

# for num in range(10):
#     insert = "INSERT into User VALUES (\"official{num}@example\.com\", \"official{num}\", \"official{num}\", \"city official\")"
#     try:
#         cur.execute(insert)
#     except pymysql.ProgrammingError:
#         print ("The following query failed:")
#         print (insert)

# for num in range(0, 3):
#     city = rand.choice(list(city_states_list))
#     state = city_states_list[city]
#     insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = \"official{num}\"), \"{city}\", \"{state}\", \"pending\")"
#     try:
#         cur.execute(insert)
#     except pymysql.ProgrammingError:
#         print ("The following query failed:")
#         print (insert)

# for num in range(3, 6):
#     city = rand.choice(list(city_states_list))
#     state = city_states_list[city]
#     insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = \"official{num}\"), \"{city}\", \"{state}\", \"rejected\")"
#     try:
#         cur.execute(insert)
#     except pymysql.ProgrammingError:
#         print ("The following query failed:")
#         print (insert)

# for num in range(6, 11):
#     city = rand.choice(list(city_states_list))
#     state = city_states_list[city]
#     insert = "INSERT into City_Official VALUES ((SELECT Username from User where Username = \"official{num}\"), \"{city}\", \"{state}\", \"approved\")"
#     try:
#         cur.execute(insert)
#     except pymysql.ProgrammingError:
#         print ("The following query failed:")
#         print (insert)

# POI Locations

# cur.execute("INSERT into POI_Location VALUES (\"Georgia Tech\", \"Atlanta\", \"Georgia\", \"30332\", \"Yes\", \"02/23/2017\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"GSU\", \"Atlanta\", \"Georgia\", \"30303\" \"No\", \"\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"Emory\", \"Atlanta\", \"Georgia\", \"30322\", \"No\", \"\")")
# cur.execute("INSERT into POI_Location VALUES (\"Uchicago\", \"Chicago\", \"Illinois\", \"60637\", \"Yes\", \"02/24/2017\")")

# # TODO: 6 POI locations

# cur.execute(
#     "INSERT into POI_Location VALUES (\"\", \"\", \"\", \"\", \"No\", \"\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"\", \"\", \"\", \"\", \"No\", \"\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"\", \"\", \"\", \"\", \"No\", \"\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"\", \"\", \"\", \"\", \"No\", \"\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"\", \"\", \"\", \"\", \"No\", \"\")")
# cur.execute(
#     "INSERT into POI_Location VALUES (\"\", \"\", \"\", \"\", \"No\", \"\")")

# Data Points

cur.execute(
    "INSERT into Data_Points VALUES (\"Georgia Tech\", \"01/31/2017 15:32\", \"12\", \"Mold\")")
cur.execute(
    "INSERT into Data_Points VALUES (\"Georgia Tech\", \"02/15/2017 16:12\", \"42\", \"Mold\")")
cur.execute(
    "INSERT into Data_Points VALUES (\"Georgia Tech\", \"02/24/2017 4:29\", \"4\", \"Air Quality\")")
cur.execute(
    "INSERT into Data_Points VALUES (\"Georgia Tech\", \"02/01/2017 3:57\", \"34\", \"Air Quality\")")


rand.randint(0,9)



rand.randint(0,9)

for num in range(9):
    insert = "INSERT into Data_Points VALUES (\"Georgia Tech\", \"01/31/2017 15:32\", \"12\", \"Mold\")")
        cur.execute(insert)
    except pymysql.ProgrammingError:
        print ("The following query failed:")
        print (insert)

TODO: 36 data points

db.commit()
db.close()
