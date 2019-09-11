from sqlalchemy import MetaData, Table, Column, Text, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from config import DATABASE_CONNECTION_URI
import json
from datetime import datetime

engine = db.create_engine(DATABASE_CONNECTION_URI)


class Database():

    def __init__(self):
        self.connection = engine.connect()
        self.Session = sessionmaker(engine)
        self.session = self.Session()

    def insertSolutions(self, n, solutions, boards):
        serial_boards = json.dumps(boards)
        timestamp = datetime.now()
        solution = Solutions(N=n, date=timestamp,
                             sols=solutions, boards=serial_boards)
        self.session.add(solution)
        self.session.commit()
        print('Solution Saved Successfully')


Base = declarative_base()


class Solutions(Base):
    """Model for saving solutions"""
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    N = Column(Integer)
    sols = Column(Integer)
    boards = Column(Text)

    def __repr__(self):
        return "<Solutions(N='%d' = sols='%d'. Boards: '%s'>" % (self.N,
                                                                 self.sols,
                                                                 self.boards)


Base.metadata.create_all(engine)


def main():
    Database()


if __name__ == "__main__":
    # execute only if run as a script
    main()
