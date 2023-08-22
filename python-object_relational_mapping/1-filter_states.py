import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_params = {
        "host": "localhost",
        "user": username,
        "passwd": password,
        "db": database,
        "port": 3306,
    }

    cur.execute("SELECT name FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
