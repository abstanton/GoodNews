# GoodNews
A news app which delivers only good news from the past 24 hours

## Oxford Hack 2020
This is a project created for the [Oxford Hack 2020](https://oxfordhack.co.uk/) by [Angus Stanton](https://github.com/abstanton) and [J Keane Quigley](https://github.com/kquigley29).

## News Sources
The news articles are obtained from [newsapi.org](https://newsapi.org/). The results are filtered by country (United Kingdom and United States) and also divided into catagories of `general`, `sports`, `technology`, `science`, `health`, `business` and `entertainment` if requested.

## Sentiment Analysis
The sentiment analysis is done through Google Cloud's language library for python. Each news article is given a sentiment score ranging from -1 to 1. The higher the score, the more positive the artice is according to the analyser.

## The App
The app is build with React-Native and is compatable with Android and iOS.

## Requirements
To run the code in the `newsData` directory, the following requirements must be met:

### Packages
The following packages are needed:  
* `flask`  
* `sqlalchemy`  
* `google-cloud-language`

To install these packages, run the following in your terminal:
```
pip3 install <package>
```
replacing `<package>` with the package name.

### Google Cloud Setup
To use the Google Cloud Services you need to follow these [instructions](https://cloud.google.com/natural-language/docs/sentiment-tutorial) to set up a Google Cloud Natural Lunguage API Project and credentials.

### News API Key
To access the news articles from [newsapi.org](https://newsapi.org/), you must first sign up and get an API key.  
The key should be copied and pasted into the file `newsData/fill.py` at the variable `api_key`.  
Demonstratively, replace the `<PASTE YOUR API KEY HERE AS A STRING>` with your key:
```Python
...
from model import Base, AllNews, GeneralNews, SportsNews, TechNews, ScienceNews, HealthNews, BusinessNews, EntertainmentNews
from news import news


api_key = <PASTE YOUR API KEY HERE AS A STRING>
url = "https://newsapi.org/v2/top-headlines?pageSize={page_size}&country={country}&category={category}&apiKey={api_key}"
...

```

## Run
Firstly chage directory in a terminal window to the newsData directory.  
To run the app, the database must be populated with the news data. To do this run the following in the terminal window:
```
python3 fill.py
```
This will take some time to finish due to the large number of news articles being fetched and analysed.  
Once it is finished, run the following in the terminal:
```
python3 api.py
```
This will allow you to access the data in the database in JSON format through your browser. Just use the url shown in the terminal window; likely http://127.0.0.1:5000.

## Finding the Correct Data
The articles can be divided into categories and filtered depending on the sentiment analysis scores.  
To look at category-specific data type http://127.0.0.1:5000/news/CATEGORY into your browser, replacing `CATEGORY` with the desired one.  
To filter out articles with a sentiment score below a certain value, use http://127.0.0.1:5000/news/CATEGORY/sentiment/MIN_SCORE, replacing `CATEGORY` as mentioned as well as `MIN_SCORE`.  
Remember, `MIN_SCORE` is a value in the range [-1, 1].  
The available categories are:
* `all`
* `general`
* `sports`
* `technology`
* `science`
* `health`
* `business`
* `entertainment`
