# app/my_project/auth/models/user.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)
