# app/my_project/auth/dao/chat_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.chat_model import Chat
from app import db

class ChatDao:
    @staticmethod
    def create_chat(json):
        new_chat = Chat.transform_from_json(json)
        db.session.add(new_chat)
        db.session.commit()
        return new_chat.transform_to_json()

    @staticmethod
    def get_chats_by_admain_id(admin_id):
        return Chat.query.filter_by(admin_id=admin_id).all()

    @staticmethod
    def get_chat_by_id(chat_id):
        return Chat.query.get(chat_id)

    @staticmethod
    def get_all_chats():
        return Chat.query.all()

    @staticmethod
    def update_chat(chat_id, new_data):
        print(chat_id)
        user_chat = Chat.get_chat_by_id(chat_id)
        print("-"*1000)
        print(user_chat)
        for key, value in new_data.items():
            setattr(user_chat, key, value)
        db.session.commit()

    @staticmethod
    def delete_chat(chat_id):
        user_chat = Chat.get_chat_by_id(chat_id)
        db.session.delete(user_chat)
        db.session.commit()