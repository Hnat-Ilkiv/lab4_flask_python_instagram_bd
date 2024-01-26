# app/my_project/auth/models/user.py
from my_project.auth.models.user_details_model import UserDetails
from my_project.auth.models.post_model import Post
from my_project.auth.models.story_model import Story
from my_project.auth.models.comment_model import Comment
from my_project.auth.models.reaction_model import Reaction
from my_project.auth.models.follower_model import Follower
from my_project.auth.models.message_model import Message
from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    user_details = db.relationship('UserDetails', backref='user', uselist=False, cascade='all, delete-orphan', single_parent=True)
    posts = db.relationship('Post', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    storys = db.relationship('Story', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    comment = db.relationship('Comment', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    reaction = db.relationship('Reaction', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    followers = db.relationship('Follower', backref='users', lazy='dynamic', cascade='all, delete-orphan', foreign_keys='Follower.user_id')
    following = db.relationship('Follower', backref='usering', lazy='dynamic', cascade='all, delete-orphan', foreign_keys='Follower.follower_id')
    sender = db.relationship('Message', backref='user_sender', lazy='dynamic', cascade='all, delete-orphan', foreign_keys='Message.sender_id')
    receiver = db.relationship('Message', backref='user_receiver', lazy='dynamic', cascade='all, delete-orphan', foreign_keys='Message.receiver_id')

    @staticmethod
    def transform_from_json(json):
        return User(id = json.get("id"), username = json["username"], email = json["email"], password_hash = json["password_hash"], date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password_hash': self.password_hash, 'date': self.date}
