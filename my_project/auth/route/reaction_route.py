# app/my_project/auth/route/reaction_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.reaction_service import ReactionService

reaction_bp = Blueprint('reaction', __name__, url_prefix='/reaction')

@reaction_bp.route('', methods=['GET'])
def get_all_reactions():
    from my_project.auth.service.reaction_service import ReactionService
    users_reactions = ReactionService.get_all_reactions()
    users_reactions_list = [user_reactions.transform_to_json() for user_reactions in users_reactions]
    return jsonify({'users_reactions': users_reactions_list})

@reaction_bp.route('/post/<int:post_id>', methods=['GET'])
def get_reactions_by_post_id(post_id):
    from my_project.auth.service.reaction_service import ReactionService
    user_reactions = ReactionService.get_reactions_by_post_id(post_id)
    if user_reactions:
        return jsonify([user_reaction.transform_to_json() for user_reaction in user_reactions])
    else:
        return jsonify({'message': 'Reactions not found'}), 404

@reaction_bp.route('/story/<int:story_id>', methods=['GET'])
def get_reactions_by_story_id(story_id):
    from my_project.auth.service.reaction_service import ReactionService
    user_reactions = ReactionService.get_reactions_by_story_id(story_id)
    if user_reactions:
        return jsonify([user_reaction.transform_to_json() for user_reaction in user_reactions])
    else:
        return jsonify({'message': 'Reactions not found'}), 404

@reaction_bp.route('/comment/<int:comment_id>', methods=['GET'])
def get_reactions_by_comment_id(comment_id):
    from my_project.auth.service.reaction_service import ReactionService
    user_reactions = ReactionService.get_reactions_by_comment_id(comment_id)
    if user_reactions:
        return jsonify([user_reaction.transform_to_json() for user_reaction in user_reactions])
    else:
        return jsonify({'message': 'Reactions not found'}), 404

@reaction_bp.route('/one/<int:reaction_id>', methods=['GET'])
def get_reaction_by_id(reaction_id):
    from my_project.auth.service.reaction_service import ReactionService
    user_reaction = ReactionService.get_reaction_by_id(reaction_id)
    if user_reaction:
        return jsonify(user_reaction.transform_to_json())
    else:
        return jsonify({'message': 'Reaction not found'}), 404

@reaction_bp.route('', methods=['POST'])
def create_reaction():
    from my_project.auth.service.reaction_service import ReactionService
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    post_id = data.get('post_id')
    story_id = data.get('story_id')
    comment_id = data.get('comment_id')
    type = data.get('type')
    new_reaction = ReactionService.create_reaction(data)
    return jsonify(new_reaction), 201

@reaction_bp.route('/one/<int:reaction_id>', methods=['PUT'])
def update_reaction(reaction_id):
    from my_project.auth.service.reaction_service import ReactionService
    user_reaction = ReactionService.get_reaction_by_id(reaction_id)
    if not user_reaction:
        return jsonify({'message': 'Reaction not found'}), 404

    data = request.json
    ReactionService.update_reaction(reaction_id, data)
    return jsonify({'message': 'Reaction updated successfully'}), 200

@reaction_bp.route('/one/<int:reaction_id>', methods=['DELETE'])
def delete_reaction(reaction_id):
    from my_project.auth.service.reaction_service import ReactionService
    user_reaction = ReactionService.get_reaction_by_id(reaction_id)
    if not user_reaction:
        return jsonify({'message': 'Reaction not found'}), 404

    ReactionService.delete_reaction(reaction_id)
    return jsonify({'message': 'Reaction deleted successfully'}), 200