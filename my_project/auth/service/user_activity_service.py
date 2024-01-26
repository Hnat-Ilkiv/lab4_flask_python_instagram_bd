# app/my_project/auth/service/user_details_service.py
from my_project.auth.dao.user_activity_dao import UserActivityDao

class UserActivityService:
    @staticmethod
    def create_user_activity(json):
        return UserActivityDao.create_user_activity(json)

    @staticmethod
    def get_user_user_activitys_by_user_id(user_id):
        return UserActivityDao.get_user_user_activitys_by_user_id(user_id)

    @staticmethod
    def get_user_user_activity_by_id(user_activity_id):
        return UserActivityDao.get_user_user_activity_by_id(user_activity_id)
    
    @staticmethod
    def get_all_users_user_activitys():
        return UserActivityDao.get_all_users_user_activitys()

    @staticmethod
    def update_user_user_activity(user_activity_id, new_data):
        UserActivityDao.update_user_user_activity(user_activity_id, new_data)

    @staticmethod
    def delete_user_user_activity(user_activity_id):
        UserActivityDao.delete_user_user_activity(user_activity_id)
