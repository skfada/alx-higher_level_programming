#!/usr/bin/python3
"""
Liists alil Staite oibjects thait conitain thie lettier a
friom thie dataibase hibtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql username> /
                                   <mysql password> /
                                   <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
