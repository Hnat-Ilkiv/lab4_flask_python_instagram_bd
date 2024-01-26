# app/my_project/auth/models/user_activity_model.py
from app import db

class UserActivity(db.Model):
    __tablename__ = 'user_activity'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_start = db.Column(db.TIMESTAMP, nullable=False)
    date_finish = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    @staticmethod
    def transform_from_json(json):
        return UserActivity(id = json.get("id"), user_id = json.get("user_id"), date_start = json.get("date_start"), date_finish = json.get("date_finish"))

    def transform_to_json(self):
        return {'id': self.id, 'user_id': self.user_id, 'date_start': self.date_start, 'date_finish': self.date_finish}
