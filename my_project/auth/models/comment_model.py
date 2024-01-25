# app/my_project/auth/models/comment.py
from my_project.auth.models.reaction_model import Reaction
from app import db

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    text = db.Column(db.Text)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    reaction = db.relationship('Reaction', backref='comment', lazy='dynamic', cascade='all, delete-orphan')

    @staticmethod
    def transform_from_json(json):
        return Comment(id = json.get("id"), user_id = json.get("user_id"), post_id = json.get("post_id"), story_id = json.get("story_id"), text = json.get("text"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'user_id': self.user_id, 'post_id': self.post_id, 'story_id': self.story_id, 'text': self.text, 'date': self.date}
