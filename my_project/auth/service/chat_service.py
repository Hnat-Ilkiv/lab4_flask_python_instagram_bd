# app/my_project/auth/service/chat_service.py
from my_project.auth.dao.chat_dao import ChatDao

class ChatService:
    @staticmethod
    def create_chat(json):
        return ChatDao.create_chat(json)

    @staticmethod
    def get_chats_by_admain_id(admin_id):
        return ChatDao.get_chats_by_admain_id(admin_id)

    @staticmethod
    def get_chat_by_id(chat_id):
        return ChatDao.get_chat_by_id(chat_id)
    
    @staticmethod
    def get_all_chats():
        return ChatDao.get_all_chats()

    @staticmethod
    def update_chat(chat_id, new_data):
        ChatDao.update_chat(chat_id, new_data)

    @staticmethod
    def delete_chat(chat_id):
        ChatDao.delete_chat(chat_id)
