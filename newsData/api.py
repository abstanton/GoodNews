from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import AllNews, GeneralNews, SportsNews, TechNews, ScienceNews, HealthNews, BusinessNews, EntertainmentNews
from model import Base
import json


app=Flask(__name__)
cors = CORS(app)
engine = create_engine("sqlite:///news.db")
Base.metadata.create_all(engine)
app.config['DEBUG'] = True


@app.route("/")
@cross_origin()
def home():
    html = """<html>
              <head>
              <style>
              h1 {text-align: center;}
              p {text-align: center;}
              </style>
              </head>

              <body>
              <h1>News API with Sentiment Analysis</h1>
              <p>Created by Angus Stanton and J Keane Quigley</p>
              <p>GitHub repository: <a href=https://www.github.com/abstanton/GoodNews>abstanton/GoodNews</a></p>
              </body>
              </html>
              """

    return html


# return articles from specified categories
@app.route("/news/<category>")
@cross_origin()
def categorisedNews(category):
    Session = sessionmaker(bind=engine)
    session = Session()
    if category == "all":
        query = session.query(AllNews).all()
    elif category == "general":
        query = session.query(GeneralNews).all()
    elif category == "sports":
        query = session.query(SportsNews).all()
    elif category == "technology":
        query = session.query(TechNews).all()
    elif category == "science":
        query = session.query(ScienceNews).all()
    elif category == "health":
        query = session.query(HealthNews).all()
    elif category == "business":
        query = session.query(BusinessNews).all()
    elif category == "entertainment":
        query = session.query(EntertainmentNews).all()
    session.close()

    r = []
    for t in query:
        r.append(t.toJson())
    
    return jsonify(r)


@app.route("/news/<category>/sentiment/<min_score>")
@cross_origin()
def goodCategotisedNews(category, min_score):
    Session = sessionmaker(bind=engine)
    session = Session()
    if category == "all":
        query = session.query(AllNews).all()
    elif category == "general":
        query = session.query(GeneralNews).all()
    elif category == "sports":
        query = session.query(SportsNews).all()
    elif category == "technology":
        query = session.query(TechNews).all()
    elif category == "science":
        query = session.query(ScienceNews).all()
    elif category == "health":
        query = session.query(HealthNews).all()
    elif category == "business":
        query = session.query(BusinessNews).all()
    elif category == "entertainment":
        query = session.query(EntertainmentNews).all()
    session.close()

    r = []
    for t in query:
        if t.sentiment_score >= float(min_score):
            r.append(t.toJson())
    
    return jsonify(r)


app.run(host='0.0.0.0')
