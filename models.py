from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

from utils import db_connect

Base = declarative_base()


class Date(Base):
    __tablename__ = 'date'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    day_of_week = Column(Integer)


db_connect(Base)
