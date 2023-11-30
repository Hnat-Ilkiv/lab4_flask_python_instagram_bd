# app/my_project/auth/controller/user_controller.py
from flask import Blueprint, jsonify, request
from my_project.auth.service.user_service import UserService

user_controller_bp = Blueprint('user_controller', __name__)

@user_controller_bp.route('/users', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email, 'date': user.date} for user in users]
    return jsonify({'users': user_list})

@user_controller_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'date': user.date})
    else:
        return jsonify({'message': 'User not found'}), 404

@user_controller_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password_hash = data.get('password_hash')  # Вам може знадобитися додаткова обробка для зберігання хеша пароля
    new_user = UserService.create_user(username, email, password_hash)
    return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email, 'date': new_user.date}), 201

@user_controller_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    UserService.update_user(user, data)
    return jsonify({'message': 'User updated successfully'}), 200

@user_controller_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    UserService.delete_user(user)
    return jsonify({'message': 'User deleted successfully'}), 200
