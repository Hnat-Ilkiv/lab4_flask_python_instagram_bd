# app/my_project/auth/dao/chat_member_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.chat_member_model import ChatMember
from app import db

class ChatMemberDao:
    @staticmethod
    def create_chat_member(json):
        new_chat_member = ChatMember.transform_from_json(json)
        db.session.add(new_chat_member)
        db.session.commit()
        return new_chat_member.transform_to_json()

    @staticmethod
    def get_user_chats(user_id):
        return ChatMember.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_in_chat(chat_id):
        return ChatMember.query.filter_by(chat_id=chat_id).all()

    @staticmethod
    def get_chat_member_by_id(chat_member_id):
        return ChatMember.query.get(chat_member_id)

    @staticmethod
    def update_chat_member(chat_member_id, new_data):
        print(chat_member_id)
        user_chat_member = ChatMember.get_chat_member_by_id(chat_member_id)
        print("-"*1000)
        print(user_chat_member)
        for key, value in new_data.items():
            setattr(user_chat_member, key, value)
        db.session.commit()

    @staticmethod
    def delete_chat_member(chat_member_id):
        user_chat_member = ChatMember.get_chat_member_by_id(chat_member_id)
        db.session.delete(user_chat_member)
        db.session.commit()