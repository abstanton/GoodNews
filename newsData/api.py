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


@app.route("/news")
@cross_origin()
def news():
    pass


app.run()
