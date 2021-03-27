#!/usr/bin/python3
""" a script that is safe from MySQL injections """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    oldinput = argv[4]
    newinput = ""
    for i in range(len(oldinput)):
        if (oldinput[i] is "\'" and i != 0):
            break
        else:
            newinput += oldinput[i]
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC"
                .format(newinput))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
