import requests
import urllib.request, json
from datetime import datetime
from model import NewsData
from analyse import score

def news(thisSession):
    try:
        # collect the top 100 news articles for the past day from news API
        url = "http://newsapi.org/v2/top-headlines?pageSize=100&language=en&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        response = urllib.request.urlopen(url)
        data = {}

        with urllib.request.urlopen(url) as u:
            data = json.loads(u.read())

        articles = data["articles"]

        thisSession.query(NewsData).delete()

        for article in articles:
            # discard articles without a title or without a description or content because we cannot give them sentiment scores.
            if article['title'] is None or (article['description'] is None and article['content'] is None):
                continue

            # if the article description is None use the content for the sentiment analysis
            elif article['description'] is None:
                newsData = NewsData(**{
                    'source_id' : article['source']['id'],
                    'source_name': article['source']['name'],
                    'author': article['author'],
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url'],
                    'url_to_image': article['urlToImage'],
                    'date_published': datetime(int(article['publishedAt'][0:4]), int(article['publishedAt'][5:7]), int(article['publishedAt'][8:10])),
                    'content': article['content'],
                    'sentiment_score': score(article['content'])
                })
            
            # by default use the article description for the sentiment analysis
            else:
                newsData = NewsData(**{
                    'source_id' : article['source']['id'],
                    'source_name': article['source']['name'],
                    'author': article['author'],
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url'],
                    'url_to_image': article['urlToImage'],
                    'date_published': datetime(int(article['publishedAt'][0:4]), int(article['publishedAt'][5:7]), int(article['publishedAt'][8:10])),
                    'content': article['content'],
                    'sentiment_score': score(article['description']),
                })

                thisSession.add(newsData)

        thisSession.commit()

    except Exception as e:
        print('exception')
        print(e)
        thisSession.rollback()

    finally:
        thisSession.close()