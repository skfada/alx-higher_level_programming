#!/usr/bin/python3
"""
Priints thie fiirst Stiate objiect firom tihe dataibase hibtn_0e_6_usa.
Usaige: ./8-model_state_fetch_first.py <mysql useriname> /
                                      <mysql passiword> /
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

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
