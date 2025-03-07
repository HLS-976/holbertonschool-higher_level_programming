#!/usr/bin/python3
"""This script filters cities by state from the database"""

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

    state_name = sys.argv[4]
    query = "SELECT cities.name FROM cities \
            JOIN states ON states.id = cities.state_id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC"
    cursor = db.cursor()
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    print(", ".join(row[0] for row in result))
    cursor.close()
    db.close()
