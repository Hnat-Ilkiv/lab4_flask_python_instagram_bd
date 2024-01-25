# app/my_project/auth/service/reaction_service.py
from my_project.auth.dao.reaction_dao import ReactionDao

class ReactionService:
    @staticmethod
    def create_reaction(json):
        return ReactionDao.create_reaction(json)

    @staticmethod
    def get_reactions_by_post_id(post_id):
        return ReactionDao.get_reactions_by_post_id(post_id)

    @staticmethod
    def get_reactions_by_story_id(story_id):
        return ReactionDao.get_reactions_by_story_id(story_id)

    @staticmethod
    def get_reactions_by_comment_id(comment_id):
        return ReactionDao.get_reactions_by_comment_id(comment_id)

    @staticmethod
    def get_reaction_by_id(reaction_id):
        return ReactionDao.get_reaction_by_id(reaction_id)
    
    @staticmethod
    def get_all_reactions():
        return ReactionDao.get_all_reactions()

    @staticmethod
    def update_reaction(reaction_id, new_data):
        ReactionDao.update_reaction(reaction_id, new_data)

    @staticmethod
    def delete_reaction(reaction_id):
        ReactionDao.delete_reaction(reaction_id)
