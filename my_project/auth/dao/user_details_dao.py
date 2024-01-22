# app/my_project/auth/dao/user_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.user_details_model import UserDetails
from app import db

class UserDetailsDao:
    @staticmethod
    def create_user_details(json):
        new_user_details = UserDetails.transform_from_json(json)
        db.session.add(new_user_details)
        db.session.commit()
        return new_user_details.transform_to_json()

    @staticmethod
    def get_user_details_by_id(user_id):
        return UserDetails.query.get(user_id)

    @staticmethod
    def get_all_users_details():
        return UserDetails.query.all()

    @staticmethod
    def update_user_details(user_id, new_data):
        print(user_id)
        user_details = UserDetailsDao.get_user_details_by_id(user_id)
        print("-"*1000)
        print(user_details)
        for key, value in new_data.items():
            setattr(user_details, key, value)
        db.session.commit()

    @staticmethod
    def delete_user_details(user_id):
        user_details = UserDetailsDao.get_user_details_by_id(user_id)
        db.session.delete(user_details)
        db.session.commit()