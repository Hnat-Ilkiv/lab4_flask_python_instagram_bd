# app/my_project/auth/service/chat_message_service.py
from my_project.auth.dao.chat_message_dao import ChatMessageDao

class ChatMessageService:
    @staticmethod
    def create_chat_message(json):
        return ChatMessageDao.create_chat_message(json)

    @staticmethod
    def get_message_chats(message_id):
        return ChatMessageDao.get_message_chats(message_id)

    @staticmethod
    def get_message_in_chat(chat_id):
        return ChatMessageDao.get_message_in_chat(chat_id)

    @staticmethod
    def get_chat_message_by_id(chat_message_id):
        return ChatMessageDao.get_chat_message_by_id(chat_message_id)

    @staticmethod
    def update_chat_message(chat_message_id, new_data):
        ChatMessageDao.update_chat_message(chat_message_id, new_data)

    @staticmethod
    def delete_chat_message(chat_message_id):
        ChatMessageDao.delete_chat_message(chat_message_id)
