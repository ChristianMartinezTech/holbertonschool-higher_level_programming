#!/usr/bin/python3
""" Script that lists all State objects from hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id)
    for states in q:
        print("{}: {}".format(states.id, states.name))

    session.close()
