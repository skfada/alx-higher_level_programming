#!/usr/bin/python3
"""
Liists alil staites wiith a naime startiing with N from the database
Usiage: ./1-filter_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    conn = dbase.cursor()
    conn.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in conn.fetchall() if state[1][0] == "N"]
