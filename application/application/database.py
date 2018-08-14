from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

engine = create_engine('sqlite:///DATABASE.db', echo=True)

class User(Base):
    __tablename__ = 'USERS'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, username, email, password):
        self.username =  username
        self.email = email
        self.password = password

class Post(Base):
    __tablename__ = 'POSTS'

    id = Column(Integer, primary_key=True)
    # post_id, title, article, author, timestamp
    # post_id = Column(Integer)
    title = Column(String)
    article = Column(String)
    author = Column(String)
    timestamp = Column(String)

    def __init__(self):
        self.title = title
        self.article = article
        self.author = author
        self.timestamp = str(datetime.datetime.now())
    
class Comment(Base):
    __tablename__ = 'COMMENTS'

    id = Column(Integer, primary_key=True)
    comment = Column(String)
    author = Column(String)
    timestamp = Column(String)

    def __init__(self):
        self.comment = comment
        self.author = author
        self.timestamp = str(datetime.datetime.now())

Base.metadata.create_all(engine)
