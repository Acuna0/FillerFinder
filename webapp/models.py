from . import db, DB_NAME
from flask_login import UserMixin
from sqlalchemy.sql import func
from os import path


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    show_name = db.Column(db.String(1000))
    eps_num = db.Column(db.String(50000))
    show_title = db.Column(db.String(50000))
    status = db.Column(db.String(500))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    shows = db.relationship('Show')

