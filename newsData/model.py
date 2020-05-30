from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, Text, Float

Base = declarative_base()

class NewsData(Base):
    __tablename__ = 'News'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    source_id = Column(Text)
    source_name = Column(Text)
    author = Column(Text)
    title = Column(Text)
    description = Column(Text)
    url = Column(Text)
    url_to_image = Column(Text)
    date_published = Column(Date)
    content = Column(Text)
    sentiment_score = Column(Float)

    def __repr__(self):
        return f'Title: {self.title}'

    def toJson(self):
        return dict(
            id = self.id,
            source_id = self.source_id,
            source_name = self.source_name,
            author = self.author,
            title = self.title,
            description = self.description,
            url = self.url,
            url_to_image = self.url_to_image,
            dest_published = self.date_published,
            content = self.content,
            sentiment_score = self.sentiment_score
        )