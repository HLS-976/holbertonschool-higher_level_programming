#!/usr/bin/python3
"""
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

    table = "states"
    query = "SELECT * FROM {} WHERE \
        name = %s ORDER BY id ASC".format(table)
    name_to_search = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
