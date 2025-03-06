#!/usr/bin/python3
"""
This script lists all states starting
with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = MySQLdb.cursors()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE \
                    'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
