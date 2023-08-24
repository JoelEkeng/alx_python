import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connection_params = {
        "host": "localhost",
        "user": username,
        "passwd": password,
        "db": database,
        "port": 3306,
    }

    try:
        db = MySQLdb.connect(**connection_params)
        cur = db.cursor()

        query = """
        SELECT *
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE name LIKE '%s'
        ORDER BY id ASC
        """
        cur.execute(query, (state_name,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()
