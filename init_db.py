from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, OperationalError
from datetime import datetime, timedelta

from models import Date
from utils import db_connect, get_or_create

Base = declarative_base()


def main():
    session = db_connect(Base)

    # check to see if there are already 100 items in the date table
    if session.query(Date).count() >= 100:
        print("Error: database already contains 100 dates")
        return

    # otherwise initialise the db with 100 days from yesterday
    date_end = datetime.today() - timedelta(days=1)
    dates = [date_end - timedelta(days=x) for x in range(0, 100)]
    for item in dates:
        date = {
            'date': item.date(),
            'day': item.day,
            'month': item.month,
            'year': item.year,
            'day_of_week': item.weekday()
        }
        get_or_create(session, Date, **date)


if __name__ == '__main__':
    main()
