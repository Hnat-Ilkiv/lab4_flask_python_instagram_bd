# app/my_project/auth/service/user_details_service.py
from my_project.auth.dao.user_details_dao import UserDetailsDao

class UserDetailsService:
    @staticmethod
    def create_user_details(json):
        return UserDetailsDao.create_user_details(json)

    @staticmethod
    def get_user_details_by_id(user_id):
        return UserDetailsDao.get_user_details_by_id(user_id)

    @staticmethod
    def get_all_users_details():
        return UserDetailsDao.get_all_users_details()

    @staticmethod
    def update_user_details(user, new_data):
        UserDetailsDao.update_user_details(user, new_data)

    @staticmethod
    def delete_user_details(user):
        UserDetailsDao.delete_user_details(user)
