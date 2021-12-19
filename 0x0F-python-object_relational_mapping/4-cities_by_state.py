#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
        )

    cur = connection.cursor()
    cur.execute("SELECT cities.id cities.name\
        FROM cities\
        INNER JOIN states ON cities.state_id = state.name\
        ORDER BY cities.id ASC;", (argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    connection.close()
