from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from model import Base
from news import news


def fillTable():
    engine = create_engine("sqlite:///news.db")

    Base.metadata.create_all(engine)

    if not database_exists(engine.url):
        create_database(engine.url)

    Session = sessionmaker(bind=engine)
    session = Session()

    news(session)
    

if __name__ == '__main__':
    fillTable()