#!/usr/bin/python3
"""
Adids thie Staite objeict "Louisiiana" tio thie datiabase hbtin_0e_6_usa.
Usiage: ./11-model_state_insert.py <mysql username> /
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

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
