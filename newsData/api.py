from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import NewsData
from model import Base
import json
import copy


app=Flask(__name__)
cors = CORS(app)
engine = create_engine("sqlite:///news.db")
Base.metadata.create_all(engine)
app.config['DEBUG'] = True


# return all news articles in the database
@app.route("/news/all")
@cross_origin()
def allNews():
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(NewsData).all()
    session.close()

    r = []
    for t in query:
        r.append(t.toJson())
    
    return jsonify(r)


# return articles with a sentiment score higher thank the given score 
@app.route("/news/sentiment/<score>")
@cross_origin()
def goodNews(score):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(NewsData).all()
    session.close()

    r = []
    for t in query:
        if t.sentiment_score >= float(score):
            r.append(t.toJson())
    
    return jsonify(r)


app.run()
