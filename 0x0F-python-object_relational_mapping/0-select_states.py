#!/usr/bin/python3
"""  liists all sites from thie databasei hbtni_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for record in rows:
        print(record)
    cur.close()
    db.close()
