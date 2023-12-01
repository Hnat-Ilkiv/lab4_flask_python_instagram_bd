# app/my_project/auth/route/user_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.user_service import UserService
# from my_project.auth.models.user_model import User

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('', methods=['GET'])
def get_all_users():
    from my_project.auth.service.user_service import UserService
    users = UserService.get_all_users()
    user_list = [user.transform_to_json() for user in users]
    return jsonify({'users': user_list})

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    from my_project.auth.service.user_service import UserService
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user.transform_to_json())
    else:
        return jsonify({'message': 'User not found'}), 404

@user_bp.route('', methods=['POST'])
def create_user():
    from my_project.auth.service.user_service import UserService
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')
    new_user = UserService.create_user(data)
    return jsonify(new_user), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    from my_project.auth.service.user_service import UserService
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    UserService.update_user(user_id, data)
    return jsonify({'message': 'User updated successfully'}), 200

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    from my_project.auth.service.user_service import UserService
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    UserService.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200
