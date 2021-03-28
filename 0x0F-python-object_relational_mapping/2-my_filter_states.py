#!/usr/bin/python3
""" a script that takes in an arg & displays all values in the states table """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE name='{}' COLLATE
                latin1_general_cs ORDER BY states.id ASC""".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
