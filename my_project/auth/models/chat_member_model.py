# app/my_project/auth/models/chat_member_model.py
from app import db

class ChatMember(db.Model):
    __tablename__ = 'chat_member'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @staticmethod
    def transform_from_json(json):
        return ChatMember(id = json.get("id"), chat_id = json.get("chat_id"), user_id = json.get("user_id"))

    def transform_to_json(self):
        return {'id': self.id, 'chat_id': self.chat_id, 'user_id': self.user_id, 'user_name': self.user.username, 'chat_name': self.chat.chat_name}
