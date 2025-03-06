#!/usr/bin/python3
"""Lists all states from the databases hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    """
    This create a connection
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
