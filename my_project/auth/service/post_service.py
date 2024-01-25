# app/my_project/auth/service/user_details_service.py
from my_project.auth.dao.post_dao import PostDao

class PostService:
    @staticmethod
    def create_post(json):
        return PostDao.create_post(json)

    @staticmethod
    def get_user_posts_by_user_id(user_id):
        return PostDao.get_user_posts_by_user_id(user_id)

    @staticmethod
    def get_user_post_by_id(post_id):
        return PostDao.get_user_post_by_id(post_id)
    
    @staticmethod
    def get_all_users_posts():
        return PostDao.get_all_users_posts()

    @staticmethod
    def update_user_post(post_id, new_data):
        PostDao.update_user_post(post_id, new_data)

    @staticmethod
    def delete_user_post(post_id):
        PostDao.delete_user_post(post_id)
