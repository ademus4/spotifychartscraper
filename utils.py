from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from config import DB_USER, DB_PASSWORD, DB_ADDRESS, DB_SCHEMA


def db_connect(base):
    engine = create_engine('mysql://{}:{}@{}/?charset=utf8'.format(
            DB_USER, DB_PASSWORD, DB_ADDRESS
    ))
    engine.execute('USE {}'.format(DB_SCHEMA))
    base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            return None
        return instance
