#!/usr/bin/python3
""" takes in the name of a state as an arg & lists all cities of that state """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM cities JOIN states ON cities.state_id=states.id
                WHERE states.name=%s ORDER BY cities.id ASC""", (argv[4],))
    query_rows = cur.fetchall()
    printcities = []
    for row in query_rows:
        if (row[4] == argv[4]):
            printcities.append(row[2])
    print(', '.join(printcities))
    cur.close()
    conn.close()
