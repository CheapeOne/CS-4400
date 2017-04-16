import MySQLdb as my

db = my.connect(host="127.0.0.1",
user="root",
passwd="root",
db="slsapp"
)

cursor = db.cursor()

# Admins

cur.execute("INSERT into User VALUES (\"admin@example\.com\", \"admin\", \"admin\", \"admin\")";)

for num in range(4)
    insert = "INSERT into User VALUES (\"admin{num}@example\.com\", \"admin{num}\", \"admin{num}\", \"admin\")";
    try:
        cur.execute(insert)
    except MySQLdb.ProgrammingError:
        print "The following query failed:"
        print insert

# City Scientists

for num in range(10)
    insert = "INSERT into User VALUES (\"scientist{num}@example\.com\", \"scientist{num}\", \"scientist{num}\", \"scientist\")";
    try:
        cur.execute(insert)
    except MySQLdb.ProgrammingError:
        print "The following query failed:"
        print insert

# City Officials

for num in range(10)
    insert = "INSERT into User VALUES (\"official{num}@example\.com\", \"official{num}\", \"official{num}\", \"official\")";
    try:
        cur.execute(insert)
    except MySQLdb.ProgrammingError:
        print "The following query failed:"
        print insert

db.commit()
db.close()
