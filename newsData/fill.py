from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from model import Base, AllNews, GeneralNews, SportsNews, TechNews, ScienceNews, HealthNews, BusinessNews, EntertainmentNews
from news import news


api_key = '7c90aa5041e84d8f9ac24b022d5a8d77'
url = "https://newsapi.org/v2/top-headlines?pageSize={page_size}&country={country}&category={category}&apiKey={api_key}"


# urls for each category
# country not specified
all_url = "http://newsapi.org/v2/top-headlines?pageSize={page_size}&language=en&apiKey={api_key}".format(page_size=100, api_key=api_key)

gb_general_url = url.format(page_size=100, country='gb', category='general', api_key=api_key)
gb_sports_url = url.format(page_size=100, country='gb', category='sports', api_key=api_key)
gb_tech_url = url.format(page_size=100, country='gb', category='technology', api_key=api_key)
gb_science_url = url.format(page_size=100, country='gb', category='science', api_key=api_key)
gb_health_url = url.format(page_size=100, country='gb', category='health', api_key=api_key)
gb_business_url = url.format(page_size=100, country='gb', category='business', api_key=api_key)
gb_entertainment_url = url.format(page_size=100, country='gb', category='entertainment', api_key=api_key)

us_general_url = url.format(page_size=100, country='us', category='general', api_key=api_key)
us_sports_url = url.format(page_size=100, country='us', category='sports', api_key=api_key)
us_tech_url = url.format(page_size=100, country='us', category='technology', api_key=api_key)
us_science_url = url.format(page_size=100, country='us', category='science', api_key=api_key)
us_health_url = url.format(page_size=100, country='us', category='health', api_key=api_key)
us_business_url = url.format(page_size=100, country='us', category='business', api_key=api_key)
us_entertainment_url = url.format(page_size=100, country='us', category='entertainment', api_key=api_key)


# add news article data to the database
def fill():
    engine = create_engine("sqlite:///news.db")

    Base.metadata.create_all(engine)

    if not database_exists(engine.url):
        create_database(engine.url)

    Session = sessionmaker(bind=engine)
    session = Session()


    # add categorised news to the db
    # all news
    news(thisSession=session, url=all_url, model=AllNews)
    # general news
    news(thisSession=session, url=gb_general_url, model=GeneralNews)
    news(thisSession=session, url=us_general_url, model=GeneralNews, delete=False)
    # sports news
    news(thisSession=session, url=gb_sports_url, model=SportsNews)
    news(thisSession=session, url=us_sports_url, model=SportsNews, delete=False)
    # tech news
    news(thisSession=session, url=gb_tech_url, model=TechNews)
    news(thisSession=session, url=us_tech_url, model=TechNews, delete=False)
    # science news
    news(thisSession=session, url=gb_science_url, model=ScienceNews)
    news(thisSession=session, url=us_science_url, model=ScienceNews, delete=False)
    # health news
    news(thisSession=session, url=gb_health_url, model=HealthNews)
    news(thisSession=session, url=us_health_url, model=HealthNews, delete=False)
    # business news
    news(thisSession=session, url=gb_business_url, model=BusinessNews)
    news(thisSession=session, url=us_business_url, model=BusinessNews, delete=False)
    # entertainment news
    news(thisSession=session, url=gb_entertainment_url, model=EntertainmentNews)
    news(thisSession=session, url=us_entertainment_url, model=EntertainmentNews, delete=False)


if __name__ == '__main__':
    fill()