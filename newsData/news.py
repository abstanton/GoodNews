import urllib.request, json
from datetime import datetime
from analyse import score


def news(thisSession, url, model, delete=True):
    try:
        # collect the top 100 general news articles for the past day from news API
        response = urllib.request.urlopen(url)
        data = {}

        with urllib.request.urlopen(url) as u:
            data = json.loads(u.read())

        articles = data["articles"]


        if delete:
            thisSession.query(model).delete()

        # to keep track of urls in the db and prevent duplicate articles
        added_urls = []

        for article in articles:
            # discard articles without a title or without a description or content because we cannot give them sentiment scores.
            # discard articles with duplicate urls to already added articles
            if article['title'] is None or (article['description'] is None and article['content'] is None) or article['url'] in added_urls:
                continue

            # if the article description is None use the content for the sentiment analysis
            elif article['description'] is None:
                newsModel = model(**{
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
                newsModel = model(**{
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

                thisSession.add(newsModel)
                added_urls.append(article['url'])

        thisSession.commit()

    except Exception as e:
        print('exception in {m}'.format(m=model))
        print(e)
        thisSession.rollback()

    finally:
        thisSession.close()
