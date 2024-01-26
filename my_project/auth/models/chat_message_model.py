# app/my_project/auth/models/chat_message_model.py
from app import db

class ChatMessage(db.Model):
    __tablename__ = 'chat_message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)

    @staticmethod
    def transform_from_json(json):
        return Message(id = json.get("id"), chat_id = json.get("chat_id"), message_id = json.get("message_id"))

    def transform_to_json(self):
        return {'id': self.id, 'chat_id': self.chat_id, 'message_id': self.message_id, 'text': self.message.text, 'chat_name': self.chat.chat_name, 'date': self.message.date}
