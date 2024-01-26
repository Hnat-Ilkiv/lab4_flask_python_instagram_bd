# app/my_project/auth/service/chat_member_service.py
from my_project.auth.dao.chat_member_dao import ChatMemberDao

class ChatMemberService:
    @staticmethod
    def create_chat_member(json):
        return ChatMemberDao.create_chat_member(json)

    @staticmethod
    def get_user_chats(user_id):
        return ChatMemberDao.get_user_chats(user_id)

    @staticmethod
    def get_user_in_chat(chat_id):
        return ChatMemberDao.get_user_in_chat(chat_id)

    @staticmethod
    def get_chat_member_by_id(chat_id, user_id):
        return ChatMemberDao.get_chat_member_by_id(chat_id, user_id)

    @staticmethod
    def update_chat_member(chat_id, user_id, new_data):
        ChatMemberDao.update_chat_member(chat_id, user_id, new_data)

    @staticmethod
    def delete_chat_member(chat_id, user_id):
        ChatMemberDao.delete_chat_member(chat_id, user_id)
