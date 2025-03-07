#!/usr/bin/python3
"""This script lists all cities from the database"""

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

    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close
    db.close()
