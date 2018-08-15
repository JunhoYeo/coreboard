from application import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) # id
    email = db.Column(db.String(120), unique=True, nullable=False) # email
    password = db.Column(db.String, unique=False, nullable=False) # password

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False, nullable=False) # title
    article = db.Column(db.String, unique=False, nullable=False) # article
    time = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __repr__(self):
        return '<Post %r>' % self.title

db.create_all()
