# app/my_project/auth/dao/user_activity_dao.py
from my_project.auth.models.user_activity_model import UserActivity
from app import db

class UserActivityDao:
    @staticmethod
    def create_user_activity(json):
        user_id = json.get('user_id')

        try:
            # Виконання вставки
            new_user_activity = UserActivity.transform_from_json(json)
            db.session.add(new_user_activity)
            db.session.commit()
            return new_user_activity.transform_to_json()

        except Exception as e:
            # Перевірка, чи помилка викликана тригером "User does not exist"
            if 'User does not exist' in str(e):
                return {'message': 'User does not exist'}, 404
            else:
                # Інші помилки можна обробляти відповідним чином
                return {'message': 'An error occurred during user activity creation'}, 500


    @staticmethod
    def get_user_user_activitys_by_user_id(user_id):
        return UserActivity.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_user_activity_by_id(user_activity_id):
        return UserActivity.query.get(user_activity_id)

    @staticmethod
    def get_all_users_user_activitys():
        return UserActivity.query.all()

    @staticmethod
    def update_user_user_activity(user_activity_id, new_data):
        print(user_activity_id)
        user_user_activity = UserActivity.get_user_user_activity_by_id(user_activity_id)
        print("-"*1000)
        print(user_user_activity)
        for key, value in new_data.items():
            setattr(user_user_activity, key, value)
        db.session.commit()

    @staticmethod
    def delete_user_user_activity(user_activity_id):
        user_user_activity = UserActivity.get_user_user_activity_by_id(user_activity_id)
        db.session.delete(user_user_activity)
        db.session.commit()