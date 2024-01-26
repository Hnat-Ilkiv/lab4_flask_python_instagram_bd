# app/my_project/auth/models/chat_member_model.py
from app import db

class ChatMember(db.Model):
    __tablename__ = 'chat_member'

    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)

    @staticmethod
    def transform_from_json(json):
        return ChatMember(chat_id = json.get("chat_id"), user_id = json.get("user_id"))

    def transform_to_json(self):
        return {'chat_id': self.chat_id, 'user_id': self.user_id, 'user_name': self.user.username, 'chat_name': self.chat.chat_name}
