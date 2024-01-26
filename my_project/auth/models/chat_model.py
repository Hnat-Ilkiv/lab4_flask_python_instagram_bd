# app/my_project/auth/models/chat.py
from my_project.auth.models.chat_member_model import ChatMember
from app import db

class Chat(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat_name = db.Column(db.String(255), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    chat_member = db.relationship('ChatMember', backref='chat', lazy='dynamic', cascade='all, delete-orphan')


    @staticmethod
    def transform_from_json(json):
        return Chat(id = json.get("id"), chat_name = json.get("chat_name"), admin_id = json.get("admin_id"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'chat_name': self.chat_name, 'admin_id': self.admin_id, 'date': self.date}
