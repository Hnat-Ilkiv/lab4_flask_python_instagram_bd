# app/my_project/auth/service/story_service.py
from my_project.auth.dao.story_dao import StoryDao

class StoryService:
    @staticmethod
    def create_story(json):
        return StoryDao.create_story(json)

    @staticmethod
    def get_user_storys_by_user_id(user_id):
        return StoryDao.get_user_storys_by_user_id(user_id)

    @staticmethod
    def get_user_story_by_id(story_id):
        return StoryDao.get_user_story_by_id(story_id)
    
    @staticmethod
    def get_all_users_storys():
        return StoryDao.get_all_users_storys()

    @staticmethod
    def update_user_story(story_id, new_data):
        StoryDao.update_user_story(story_id, new_data)

    @staticmethod
    def delete_user_story(story_id):
        StoryDao.delete_user_story(story_id)
