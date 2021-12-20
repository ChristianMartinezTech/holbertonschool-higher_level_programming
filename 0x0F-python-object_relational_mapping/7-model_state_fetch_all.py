#!/usr/bin/python3
""" Script that lists all State objects from hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine) """Engine Created"""

    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State).oder_by(State.id):
        print("{}: {}".format(state.id, state.name))
    
    session.close()
