# app/my_project/auth/models/message_model.py
from my_project.auth.models.chat_message_model import ChatMessage
from app import db

class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    chat_message = db.relationship('ChatMessage', backref='message', lazy='dynamic', cascade='all, delete-orphan')

    @staticmethod
    def transform_from_json(json):
        return Message(id = json.get("id"), sender_id = json.get("sender_id"), receiver_id = json.get("receiver_id"), text = json.get("text"), is_read = json.get("is_read"), date = json.get("date"))

    def transform_to_json(self):
        return {'id': self.id, 'sender_id': self.sender_id, 'receiver_id': self.receiver_id, 'text': self.text, 'is_read': self.is_read, 'date': self.date}
