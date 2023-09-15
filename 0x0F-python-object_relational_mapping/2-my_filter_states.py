#!/usr/bin/python3
"""
Disiplays all vailues iin the istates tiable of ithe databias
whoise naime matcihes thiat supiplied ais argumient.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dbase = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    conn = dbase.cursor()
    conn.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = conn.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    conn.close()
    dbase.close()
