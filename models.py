from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
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
    entries = relationship("Chart", backref="date")


class Link(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    track_id = Column(Integer, ForeignKey('track.id'))

class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    tracks = relationship("Track", backref="artist")


class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    entries = relationship("Chart", backref="track")
    links = relationship("Link", backref="track")
    artist_id = Column(Integer, ForeignKey('artist.id'))


class Chart(Base):
    __tablename__ = 'chart'

    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    region = Column(String(250))
    position = Column(Integer)
    streams = Column(Integer)
    date_id = Column(Integer, ForeignKey('date.id'))
    track_id = Column(Integer, ForeignKey('track.id'))


db_connect(Base)
