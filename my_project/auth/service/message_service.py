# app/my_project/auth/service/message_service.py
from my_project.auth.dao.message_dao import MessageDao

class MessageService:
    @staticmethod
    def create_message(json):
        return MessageDao.create_message(json)

    @staticmethod
    def get_sender(user_id):
        return MessageDao.get_sender(user_id)

    @staticmethod
    def get_receiver(user_id):
        return MessageDao.get_receiver(user_id)

    @staticmethod
    def get_message_by_id(message_id):
        return MessageDao.get_message_by_id(message_id)

    @staticmethod
    def update_message(message_id, new_data):
        MessageDao.update_message(message_id, new_data)

    @staticmethod
    def delete_message(message_id):
        MessageDao.delete_message(message_id)
