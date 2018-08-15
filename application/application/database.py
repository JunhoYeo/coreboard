from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) # id
    email = db.Column(db.String(120), unique=True, nullable=False) # email
    password = db.Column(db.String, unique=False, nullable=False) # password

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()
