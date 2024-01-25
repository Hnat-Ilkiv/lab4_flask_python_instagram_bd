# app/my_project/auth/models/follower_model.py
from app import db

class Follower(db.Model):
    __tablename__ = 'follower'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    @staticmethod
    def transform_from_json(json):
        return Follower(id = json.get("id"), user_id = json.get("user_id"), follower_id = json.get("follower_id"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'user_id': self.user_id, 'follower_id': self.follower_id, 'date': self.date}
