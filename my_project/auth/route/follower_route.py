# app/my_project/auth/route/follower_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.follower_service import FollowerService

follower_bp = Blueprint('follower', __name__, '')

@follower_bp.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id):
    from my_project.auth.service.follower_service import FollowerService
    user_followers = FollowerService.get_followers(user_id)
    if user_followers:
        return jsonify([user_follower.transform_to_json() for user_follower in user_followers])
    else:
        return jsonify({'message': 'Followers not found'}), 404

@follower_bp.route('/following/<int:user_id>', methods=['GET'])
def get_following(user_id):
    from my_project.auth.service.follower_service import FollowerService
    user_followers = FollowerService.get_following(user_id)
    if user_followers:
        return jsonify([user_follower.transform_to_json() for user_follower in user_followers])
    else:
        return jsonify({'message': 'Followers not found'}), 404

@follower_bp.route('/follower/<int:follower_id>', methods=['GET'])
def get_follower_by_id(follower_id):
    from my_project.auth.service.follower_service import FollowerService
    user_follower = FollowerService.get_follower_by_id(follower_id)
    if user_follower:
        return jsonify(user_follower.transform_to_json())
    else:
        return jsonify({'message': 'Follower not found'}), 404

@follower_bp.route('/follower', methods=['POST'])
def create_follower():
    from my_project.auth.service.follower_service import FollowerService
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    follower_id = data.get('follower_id')
    new_follower = FollowerService.create_follower(data)
    return jsonify(new_follower), 201

@follower_bp.route('/follower/<int:follower_id>', methods=['PUT'])
def update_follower(follower_id):
    from my_project.auth.service.follower_service import FollowerService
    user_follower = FollowerService.get_follower_by_id(follower_id)
    if not user_follower:
        return jsonify({'message': 'Follower not found'}), 404

    data = request.json
    FollowerService.update_follower(follower_id, data)
    return jsonify({'message': 'Follower updated successfully'}), 200

@follower_bp.route('/follower/<int:follower_id>', methods=['DELETE'])
def delete_follower(follower_id):
    from my_project.auth.service.follower_service import FollowerService
    user_follower = FollowerService.get_follower_by_id(follower_id)
    if not user_follower:
        return jsonify({'message': 'Follower not found'}), 404

    FollowerService.delete_follower(follower_id)
    return jsonify({'message': 'Follower deleted successfully'}), 200