# app/my_project/auth/dao/post_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.story_model import Story
from app import db

class StoryDao:
    @staticmethod
    def create_story(json):
        new_story = Story.transform_from_json(json)
        db.session.add(new_story)
        db.session.commit()
        return new_story.transform_to_json()

    @staticmethod
    def get_user_storys_by_user_id(user_id):
        return Story.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_story_by_id(story_id):
        return Story.query.get(story_id)

    @staticmethod
    def get_all_users_storys():
        return Story.query.all()

    @staticmethod
    def update_user_story(story_id, new_data):
        print(story_id)
        user_story = Story.get_user_story_by_id(story_id)
        print("-"*1000)
        print(user_story)
        for key, value in new_data.items():
            setattr(user_story, key, value)
        db.session.commit()

    @staticmethod
    def delete_user_story(story_id):
        user_story = Story.get_user_story_by_id(story_id)
        db.session.delete(user_story)
        db.session.commit()