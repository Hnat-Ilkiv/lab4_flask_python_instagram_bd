# app/my_project/auth/dao/comment_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.comment_model import Comment
from app import db

class CommentDao:
    @staticmethod
    def create_comment(json):
        new_comment = Comment.transform_from_json(json)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment.transform_to_json()

    @staticmethod
    def get_comments_by_post_id(post_id):
        return Comment.query.filter_by(post_id=post_id).all()

    @staticmethod
    def get_comments_by_story_id(story_id):
        return Comment.query.filter_by(story_id=story_id).all()

    @staticmethod
    def get_comment_by_id(comment_id):
        return Comment.query.get(comment_id)

    @staticmethod
    def get_all_users_comments():
        return Comment.query.all()

    @staticmethod
    def update_user_comment(comment_id, new_data):
        print(comment_id)
        user_comment = Comment.get_comment_by_id(comment_id)
        print("-"*1000)
        print(user_comment)
        for key, value in new_data.items():
            setattr(user_comment, key, value)
        db.session.commit()

    @staticmethod
    def delete_comment(comment_id):
        user_comment = Comment.get_comment_by_id(comment_id)
        db.session.delete(user_comment)
        db.session.commit()