import MySQLdb

b = MySQLdb.connect(host=localhost, port=3306, db=hbtn_0e_0_usa)

cur = db.cursor()

cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print ("%s," % col)
    print ("\n")