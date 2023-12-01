# app/my_project/auth/dao/user_dao.py
from my_project.auth.models.user_model import User
from app import db

class UserDao:
    @staticmethod
    def create_user(json):
        new_user = User.transform_from_json(json)
        db.session.add(new_user)
        db.session.commit()
        return new_user.transform_to_json()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, new_data):
        print(user_id)
        user = UserDao.get_user_by_id(user_id)
        print("-"*1000)
        print(user)
        for key, value in new_data.items():
            setattr(user, key, value)
        db.session.commit()

    @staticmethod
    def delete_user(user_id):
        user = UserDao.get_user_by_id(user_id)
        db.session.delete(user)
        db.session.commit()
