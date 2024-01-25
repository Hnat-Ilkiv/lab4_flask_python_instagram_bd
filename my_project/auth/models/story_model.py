# app/my_project/auth/models/story.py
from app import db

class Story(db.Model):
    __tablename__ = 'story'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    story_url = db.Column(db.String(255), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    comment = db.relationship('Comment', backref='story', lazy='dynamic', cascade='all, delete-orphan')

    @staticmethod
    def transform_from_json(json):
        return Post(id = json.get("id"), user_id = json.get("user_id"), story_url = json.get("story_url"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'user_id': self.user_id, 'story_url': self.story_url, 'date': self.date}
