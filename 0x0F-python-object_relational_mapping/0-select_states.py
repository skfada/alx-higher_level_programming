#!/usr/bin/python3

'''
    - this script connect to the root database
    - it list all the states in the database
    - Usage: ./0-select_states.py <user> <password> <database>
'''
import sys
import MySQLdb

conn = MySQLdb.connect(
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    port=3306
)
cur = conn.cursor()
query = 'SELECT * FROM states WHERE id < 6'
cur.execute(query)
query_rows = cur.fetchall()

if __name__ == '__main__':
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
