# app/my_project/auth/service/user_service.py
from my_project.auth.dao.user_dao import UserDao

class UserService:
    @staticmethod
    def create_user(json):
        return UserDao.create_user(json)

    @staticmethod
    def get_user_by_id(user_id):
        return UserDao.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        return UserDao.get_all_users()

    @staticmethod
    def update_user(user, new_data):
        UserDao.update_user(user, new_data)

    @staticmethod
    def delete_user(user):
        UserDao.delete_user(user)
