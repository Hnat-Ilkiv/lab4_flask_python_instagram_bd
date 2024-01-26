# app/my_project/auth/dao/chat_message_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.chat_message_model import ChatMessage
from sqlalchemy import desc
from app import db

class ChatMessageDao:
    @staticmethod
    def create_chat_message(json):
        new_chat_message = ChatMessage.transform_from_json(json)
        db.session.add(new_chat_message)
        db.session.commit()
        return new_chat_message.transform_to_json()

    @staticmethod
    def get_message_chats(message_id):
        return ChatMessage.query.filter_by(message_id=message_id).all()

    @staticmethod
    def get_message_in_chat(chat_id):
        return ChatMessage.query.filter_by(chat_id=chat_id).order_by(desc(ChatMessage.message_id)).all()

    @staticmethod
    def get_chat_message_by_id(chat_message_id):
        return ChatMessage.query.get(chat_message_id)

    @staticmethod
    def update_chat_message(chat_message_id, new_data):
        print(chat_message_id)
        user_chat_message = ChatMessage.get_chat_message_by_id(chat_message_id)
        print("-"*1000)
        print(user_chat_message)
        for key, value in new_data.items():
            setattr(user_chat_message, key, value)
        db.session.commit()

    @staticmethod
    def delete_chat_message(chat_message_id):
        user_chat_message = ChatMessage.get_chat_message_by_id(chat_message_id)
        db.session.delete(user_chat_message)
        db.session.commit()