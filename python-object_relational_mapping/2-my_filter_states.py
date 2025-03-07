#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    name_to_search = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE \
        name LIKE BINARY '%{}' ORDER BY states.id ASC".format(name_to_search)
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
