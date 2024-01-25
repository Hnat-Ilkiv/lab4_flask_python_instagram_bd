# app/my_project/auth/models/post.py
from app import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    caption = db.Column(db.Text)
    image_url = db.Column(db.String(255), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)


    @staticmethod
    def transform_from_json(json):
        return Post(id = json.get("id"), user_id = json.get("user_id"), caption = json.get("caption"), image_url = json.get("image_url"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'user_id': self.user_id, 'caption': self.caption, 'image_url': self.image_url, 'date': self.date}
