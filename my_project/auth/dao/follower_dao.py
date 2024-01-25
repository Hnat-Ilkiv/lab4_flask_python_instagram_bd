# app/my_project/auth/dao/follower_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.follower_model import Follower
from app import db

class FollowerDao:
    @staticmethod
    def create_follower(json):
        new_follower = Follower.transform_from_json(json)
        db.session.add(new_follower)
        db.session.commit()
        return new_follower.transform_to_json()

    @staticmethod
    def get_followers(user_id):
        return Follower.query.filter_by(follower_id=user_id).all()

    @staticmethod
    def get_following(user_id):
        return Follower.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_follower_by_id(follower_id):
        return Follower.query.get(follower_id)

    @staticmethod
    def update_follower(follower_id, new_data):
        print(follower_id)
        user_follower = Follower.get_follower_by_id(follower_id)
        print("-"*1000)
        print(user_follower)
        for key, value in new_data.items():
            setattr(user_follower, key, value)
        db.session.commit()

    @staticmethod
    def delete_follower(follower_id):
        user_follower = Follower.get_follower_by_id(follower_id)
        db.session.delete(user_follower)
        db.session.commit()