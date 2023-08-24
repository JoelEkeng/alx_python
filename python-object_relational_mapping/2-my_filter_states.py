import sys
import MySQLdb

def search_states_by_name(username, password, database, state_name):
    connection_params = {
        "host": "localhost",
        "user": username,
        "passwd": password,
        "db": database,
        "port": 3306,
    }

    try:
        db = MySQLdb.connect(**connection_params)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        search_states_by_name(username, password, database, state_name)
