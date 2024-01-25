# app/my_project/auth/route/story_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.story_service import StoryService

story_bp = Blueprint('story', __name__, url_prefix='/story')

@story_bp.route('', methods=['GET'])
def get_all_users_storys():
    from my_project.auth.service.story_service import StoryService
    users_storys = StoryService.get_all_users_storys()
    users_storys_list = [user_storys.transform_to_json() for user_storys in users_storys]
    return jsonify({'users_storys': users_storys_list})

@story_bp.route('/<int:user_id>', methods=['GET'])
def get_user_storys_by_user_id(user_id):
    from my_project.auth.service.story_service import StoryService
    user_storys = StoryService.get_user_storys_by_user_id(user_id)
    if user_storys:
        return jsonify([user_story.transform_to_json() for user_story in user_storys])
    else:
        return jsonify({'message': 'Storys not found'}), 404

@story_bp.route('/<int:user_id>/<int:story_id>', methods=['GET'])
def get_user_story_by_id(user_id, story_id):
    from my_project.auth.service.story_service import StoryService
    user_story = StoryService.get_user_story_by_id(story_id)
    if user_story and user_story.user_id == user_id:
        return jsonify(user_story.transform_to_json())
    else:
        return jsonify({'message': 'Story not found'}), 404

@story_bp.route('', methods=['POST'])
def create_story():
    from my_project.auth.service.story_service import StoryService
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    caption = data.get('caption')
    image_url = data.get('image_url')
    new_story = StoryService.create_story(data)
    return jsonify(new_story), 201

@story_bp.route('/<int:user_id>/<int:story_id>', methods=['PUT'])
def update_user_story(user_id, story_id):
    from my_project.auth.service.story_service import StoryService
    user_story = StoryService.get_user_story_by_id(story_id)
    if not user_story or user_story.user_id != user_id:
        return jsonify({'message': 'Story not found'}), 404

    data = request.json
    StoryService.update_user_story(story_id, data)
    return jsonify({'message': 'Story updated successfully'}), 200

@story_bp.route('/<int:user_id>/<int:story_id>', methods=['DELETE'])
def delete_user_story(user_id, story_id):
    from my_project.auth.service.story_service import StoryService
    user_story = StoryService.get_user_story_by_id(story_id)
    if not user_story or user_story.user_id != user_id:
        return jsonify({'message': 'Story not found'}), 404

    StoryService.delete_user_story(story_id)
    return jsonify({'message': 'Story deleted successfully'}), 200