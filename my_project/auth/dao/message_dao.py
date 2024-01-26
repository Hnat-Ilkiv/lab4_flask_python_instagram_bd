# app/my_project/auth/dao/message_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.message_model import Message
from app import db

class MessageDao:
    @staticmethod
    def create_message(json):
        new_message = Message.transform_from_json(json)
        db.session.add(new_message)
        db.session.commit()
        return new_message.transform_to_json()

    @staticmethod
    def get_sender(user_id):
        return Message.query.filter_by(sender_id=user_id).all()

    @staticmethod
    def get_receiver(user_id):
        return Message.query.filter_by(receiver_id=user_id).all()

    @staticmethod
    def get_message_by_id(message_id):
        return Message.query.get(message_id)

    @staticmethod
    def update_message(message_id, new_data):
        print(message_id)
        user_message = Message.get_message_by_id(message_id)
        print("-"*1000)
        print(user_message)
        for key, value in new_data.items():
            setattr(user_message, key, value)
        db.session.commit()

    @staticmethod
    def delete_message(message_id):
        user_message = Message.get_message_by_id(message_id)
        db.session.delete(user_message)
        db.session.commit()