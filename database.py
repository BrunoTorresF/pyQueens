from sqlalchemy import MetaData, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from config import DATABASE_CONNECTION_URI
import json

engine = db.create_engine(DATABASE_CONNECTION_URI)


class Database():

    def __init__(self):
        self.connection = engine.connect()
        self.Session = sessionmaker(engine)
        self.session = self.Session()
        print("DB created")

    def insertSolutions(self, n, solutions, boards):
        serial_boards = json.dumps(boards)
        solution = Solutions(N=n, sols=solutions, boards=serial_boards)
        self.session.add(solution)
        self.session.commit()


Base = declarative_base()


class Solutions(Base):
    """Model for saving solutions"""
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    N = Column(Integer)
    sols = Column(Integer)
    boards = Column(String)

    def __repr__(self):
        return "<Solutions(N='%d' = sols='%d'. Boards: '%s'>" % (self.N, self.sols, self.boards)


Base.metadata.create_all(engine)


def main():
    Database()


if __name__ == "__main__":
    # execute only if run as a script
    main()
