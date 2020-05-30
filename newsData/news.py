import requests
import urllib.request, json
from datetime import datetime
from model import NewsData

def news(thisSession):
    try:
        url = "http://newsapi.org/v2/top-headlines?pageSize=100&language=en&apiKey=7c90aa5041e84d8f9ac24b022d5a8d77"
        response = urllib.request.urlopen(url)
        data = {}

        with urllib.request.urlopen(url) as u:
            data = json.loads(u.read())

        articles = data["articles"]

        thisSession.query(NewsData).delete()

        for article in articles:
            newsData = NewsData(**{
                'source_id' : article['source']['id'],
                'source_name': article['source']['name'],
                'author': article['author'],
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'url_to_image': article['urlToImage'],
                'date_published': datetime(int(article['publishedAt'][0:4]), int(article['publishedAt'][5:7]), int(article['publishedAt'][8:10])),
                'content': article['content']
            })

            thisSession.add(newsData)

        thisSession.commit()

    except Exception as e:
        print('error')
        print(e)
        thisSession.rollback()

    finally:
        thisSession.close()