import requests
import csv
import logging
import sys
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, OperationalError
from datetime import datetime, timedelta

from models import Date, Artist, Track, Chart
from utils import db_connect, get_or_create

Base = declarative_base()

file_headers = ['Position', 'Track Name', 'Artist', 'Streams', 'URL']

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    stream=sys.stdout
)


def main():
    session = db_connect(Base)

    region = 'gb'
    dates = session.query(Date).all()

    for date in dates:
        date_str = datetime.strftime(date.date, '%Y-%m-%d')

        url_base = 'https://spotifycharts.com/regional/{}/daily/{}/download'
        url = url_base.format(region, date_str)
        logging.info('URL: {}'.format(url))

        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            continue
        text_data = r.text.encode('ascii', 'ignore').splitlines()
        reader = csv.reader(text_data, delimiter=',')
        data = [line for line in reader]
        headers = data.pop(0)
        if headers == file_headers:
            for line in data:
                save_objects(session, line, region, date)
            time.sleep(10)
        else:
            logging.info('Error with file! Incorrect headers')


def save_objects(session, data, region, date):
    position, track_name, artist_name, streams, url = data
    artist = get_or_create(session, Artist, name=artist_name)

    track_vals = {
        'title': track_name,
        'url': url,
        'artist': artist
    }
    track = get_or_create(session, Track, **track_vals)

    chart_vals = {
        'type': 'top200',
        'region': region,
        'position': position,
        'streams': streams,
        'date': date,
        'track': track
    }
    chart = get_or_create(session, Chart, **chart_vals)

if __name__ == '__main__':
    main()
