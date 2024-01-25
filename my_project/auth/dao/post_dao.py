# app/my_project/auth/dao/post_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.post_model import Post
from app import db

class PostDao:
    @staticmethod
    def create_post(json):
        new_post = Post.transform_from_json(json)
        db.session.add(new_post)
        db.session.commit()
        return new_post.transform_to_json()

    @staticmethod
    def get_user_posts_by_user_id(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_post_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def get_all_users_posts():
        return Post.query.all()

    @staticmethod
    def update_user_post(post_id, new_data):
        print(post_id)
        user_post = Post.get_user_post_by_id(post_id)
        print("-"*1000)
        print(user_post)
        for key, value in new_data.items():
            setattr(user_post, key, value)
        db.session.commit()

    @staticmethod
    def delete_user_post(post_id):
        user_post = Post.get_user_post_by_id(post_id)
        db.session.delete(user_post)
        db.session.commit()