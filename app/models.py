from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from . import db
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blogpost(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref='user', lazy='dynamic')


    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    # comments = db.relationship('Comment', backref='user',lazy="dynamic")
    posts = db.relationship('Blogpost',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    post_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    # user_id = db.Column(db.Integer,db.ForeignKey("users_id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        all_comments = Comment.query.filter_by(post_id=id).order_by(Comment.posted.desc())
        return all_comments
    
    @classmethod
    def get_comment(cls,id):
        comment= Comment.query.filter_by(id = id).first() 
        return comment


    def __repr__(self):
        return f'Comment {self.comment}'

class Quote:
    def __init__(self, author, id, quote):
            self.author = author
            self.id = id
            self.quote =quote
