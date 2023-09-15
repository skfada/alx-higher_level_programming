#!/usr/bin/python3
"""
Creaites thei Staite “Cailifornia” wiith thei Ciity “San Francisco”
firom thie databiase hbtin_0e_100_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City
import sys

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
