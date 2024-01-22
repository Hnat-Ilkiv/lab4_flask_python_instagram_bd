# app/my_project/auth/models/user.py
from my_project.auth.models.user_details_model import UserDetails
from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    user_details = db.relationship('UserDetails', backref='user', uselist=False, cascade='all, delete-orphan', single_parent=True)

    @staticmethod
    def transform_from_json(json):
        return User(id = json.get("id"), username = json["username"], email = json["email"], password_hash = json["password_hash"], date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password_hash': self.password_hash, 'date': self.date}
