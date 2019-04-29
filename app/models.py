from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

#Models
class User(db.Model):
    __tablename__ = 'users'

    uuid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, unique=True)
    posts = db.relationship('Post', backref='author')
    events = db.relationship('Event', backref='manager')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    __tablename__ = 'posts'

    uuid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.uuid'))

    def __repr__(self):
        return '<Post %r>' % self.title

class Event(db.Model):
    __tablename__ = 'events'
    
    uuid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    description = db.Column(db.Text)
    manager_id = db.Column(db.Integer, db.ForeignKey('users.uuid'))

    def __repr__(self):
        return '<Event %r' % self.title 
