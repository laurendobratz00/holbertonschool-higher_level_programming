#!/usr/bin/python3
""" a script that lists all states with a name starting with N """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' COLLATE
                latin1_general_cs  ORDER BY id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
