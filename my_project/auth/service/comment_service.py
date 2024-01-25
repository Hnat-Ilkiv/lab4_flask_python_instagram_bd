# app/my_project/auth/service/comment_service.py
from my_project.auth.dao.comment_dao import CommentDao

class CommentService:
    @staticmethod
    def create_comment(json):
        return CommentDao.create_comment(json)

    @staticmethod
    def get_comments_by_post_id(post_id):
        return CommentDao.get_comments_by_post_id(post_id)

    @staticmethod
    def get_comments_by_story_id(story_id):
        return CommentDao.get_comments_by_story_id(story_id)

    @staticmethod
    def get_comment_by_id(comment_id):
        return CommentDao.get_comment_by_id(comment_id)
    
    @staticmethod
    def get_all_users_comments():
        return CommentDao.get_all_users_comments()

    @staticmethod
    def update_user_comment(comment_id, new_data):
        CommentDao.update_user_comment(comment_id, new_data)

    @staticmethod
    def delete_comment(comment_id):
        CommentDao.delete_comment(comment_id)
