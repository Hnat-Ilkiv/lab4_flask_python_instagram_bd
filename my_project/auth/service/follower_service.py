# app/my_project/auth/service/follower_service.py
from my_project.auth.dao.follower_dao import FollowerDao

class FollowerService:
    @staticmethod
    def create_follower(json):
        return FollowerDao.create_follower(json)

    @staticmethod
    def get_followers(user_id):
        return FollowerDao.get_followers(user_id)

    @staticmethod
    def get_following(user_id):
        return FollowerDao.get_following(user_id)

    @staticmethod
    def get_follower_by_id(follower_id):
        return FollowerDao.get_follower_by_id(follower_id)

    @staticmethod
    def update_follower(follower_id, new_data):
        FollowerDao.update_follower(follower_id, new_data)

    @staticmethod
    def delete_follower(follower_id):
        FollowerDao.delete_follower(follower_id)
