# app/my_project/auth/dao/reaction_dao.py
from my_project.auth.models.user_model import User
from my_project.auth.models.reaction_model import Reaction
from app import db

class ReactionDao:
    @staticmethod
    def create_reaction(json):
        new_reaction = Reaction.transform_from_json(json)
        db.session.add(new_reaction)
        db.session.commit()
        return new_reaction.transform_to_json()

    @staticmethod
    def get_reactions_by_post_id(post_id):
        return Reaction.query.filter_by(post_id=post_id).all()

    @staticmethod
    def get_reactions_by_story_id(story_id):
        return Reaction.query.filter_by(story_id=story_id).all()

    @staticmethod
    def get_reactions_by_comment_id(comment_id):
        return Reaction.query.filter_by(comment_id=comment_id).all()

    @staticmethod
    def get_reaction_by_id(reaction_id):
        return Reaction.query.get(reaction_id)

    @staticmethod
    def get_all_reactions():
        return Reaction.query.all()

    @staticmethod
    def update_reaction(reaction_id, new_data):
        print(reaction_id)
        user_reaction = Reaction.get_reaction_by_id(reaction_id)
        print("-"*1000)
        print(user_reaction)
        for key, value in new_data.items():
            setattr(user_reaction, key, value)
        db.session.commit()

    @staticmethod
    def delete_reaction(reaction_id):
        user_reaction = Reaction.get_reaction_by_id(reaction_id)
        db.session.delete(user_reaction)
        db.session.commit()