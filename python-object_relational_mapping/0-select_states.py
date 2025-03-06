#!/usr/bin/python3
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

    table = "states"
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM {table} \
            ORDER BY {table}.id"
    )
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
