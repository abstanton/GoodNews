from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from model import Base, AllNews, GeneralNews, SportsNews, TechNews, ScienceNews, HealthNews, BusinessNews, EntertainmentNews
from news import news


# urls for each category
# country not specified
all_url = "http://newsapi.org/v2/top-headlines?pageSize=100&language=en&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"

# country=gb
gb_general_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=general&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
gb_sports_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=sports&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
gb_tech_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=technology&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
gb_science_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=science&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
gb_health_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=health&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
gb_business_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=business&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
gb_entertainment_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=gb&category=entertainment&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"

# country=us
us_general_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=general&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
us_sports_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=sports&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
us_tech_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=technology&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
us_science_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=science&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
us_health_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=health&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
us_business_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=business&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
us_entertainment_url = "https://newsapi.org/v2/top-headlines?pageSize=100&country=us&category=entertainment&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"


# add news article data to the database
def fillTable():
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
    fillTable()