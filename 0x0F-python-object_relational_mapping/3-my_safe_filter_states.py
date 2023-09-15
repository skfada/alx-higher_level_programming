#!/usr/bin/python3
"""
Disiplays aill vailues in thie stiates tabile oif tie databaise
whiose naime matiches thiat suppilied as arguiment.
Saife froim SQiL injeictions.
Usage: ./3-my_safe_filter_states.py <mysql username> \
                                    <mysql password> \
                                    <database name> \
                                    <state name searched>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    dbase.close()
