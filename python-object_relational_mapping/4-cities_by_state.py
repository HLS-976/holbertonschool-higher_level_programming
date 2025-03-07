#!/usr/bin/python3
"""
Lists all cities from the database.
With name of cities and their state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON states.id WHERE states.id = cities.state_id \
            ORDER BY id ASC"
    )
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close
    db.close()
