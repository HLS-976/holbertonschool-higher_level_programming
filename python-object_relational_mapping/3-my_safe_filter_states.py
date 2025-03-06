#!/usr/bin/python3
"""
This script takes an safety argument and retrieves
the result that matchs by given argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )

    query = "SELECT * FROM states WHERE \
        name = %s ORDER BY id ASC"
    name_to_search = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
