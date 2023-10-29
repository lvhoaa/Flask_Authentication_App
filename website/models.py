from website import db 
from flask_login import UserMixin 
from sqlalchemy.sql import func


# after logging in, user can generate notes like to-do-list 
class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) # one-to-many relationships

class User (db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(50))
    first_name= db.Column(db.String(150))
    # every time create a note, will add note id to the user table # LIST 
    notes = db.relationship('Note')