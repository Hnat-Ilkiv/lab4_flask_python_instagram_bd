# app/my_project/auth/dao/user_dao.py
from my_project.auth.models.user_model import User

class UserDao:
    @staticmethod
    def create_user(username, email, password_hash):
        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user, new_data):
        for key, value in new_data.items():
            setattr(user, key, value)
        db.session.commit()

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
