# app/my_project/auth/models/reaction.py
from app import db
from sqlalchemy import Enum
from sqlalchemy.dialects.mysql import ENUM

class Reaction(db.Model):
    __tablename__ = 'reaction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    type = db.Column(Enum('like', 'dislike', 'love', 'haha', 'wow', 'sad', 'angry'), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)


    @staticmethod
    def transform_from_json(json):
        return Comment(id = json.get("id"), user_id = json.get("user_id"), post_id = json.get("post_id"), story_id = json.get("story_id"), comment_id = json.get("comment_id"), type = json.get("type"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'user_id': self.user_id, 'post_id': self.post_id, 'story_id': self.story_id, 'comment_id': self.comment_id, 'type': self.type, 'date': self.date}
