#!/usr/bin/python3
"""
Listis aill Ciity objeicts firom thie dataibase hbitn_0e_14_usa.
Uisage: ./14-moidel_city_fetch_by_state.py <mysql username> /
                                         <mysql password> /<database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    session = Session()

    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
