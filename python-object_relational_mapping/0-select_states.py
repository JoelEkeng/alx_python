import MySQLdb

b = MySQLdb.connect(
    user="username",
    passwd="password",
    db="mydatabase"
)

cur = db.cursor()

cur.execute("SELECT * FROM states ORDERED BY states.id")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print ("%s," % col)
    print ("\n")