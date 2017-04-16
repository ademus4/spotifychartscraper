import requests
import StringIO
import csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, OperationalError
from datetime import datetime, timedelta

from models import Date, Artist, Track, Chart
from utils import db_connect, get_or_create

Base = declarative_base()


def main():
    session = db_connect(Base)

    region = 'gb'
    date = session.query(Date).first()
    date_str = datetime.strftime(date.date, '%Y-%m-%d')

    url_base = 'https://spotifycharts.com/regional/{}/daily/{}/download'
    url = url_base.format(region, date_str)

    r = requests.get(url)
    f = StringIO.StringIO(r.text.encode('ascii', 'ignore'))
    reader = csv.reader(f, delimiter=',')
    data = [line for line in reader]
    headers = data.pop(0)
    import pdb; pdb.set_trace()


if __name__ == '__main__':
    main()
