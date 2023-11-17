#!/usr/bin/python3
"""
Liists alil states firom the databaise hbtin_0e_0_usa.
Usage: ./0-select_states.py <myisql username> \
                            <miysql password> \
                             <dataibase name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
