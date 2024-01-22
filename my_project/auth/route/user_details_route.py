# app/my_project/auth/route/user_details_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.user_details_service import UserDetailsService
# from my_project.auth.models.user_details_model import UserDetails

user_details_bp = Blueprint('users_details', __name__, url_prefix='/users_details')

@user_details_bp.route('', methods=['GET'])
def get_all_users_details():
    from my_project.auth.service.user_details_service import UserDetailsService
    users_details = UserDetailsService.get_all_users_details()
    user_details_list = [user_details.transform_to_json() for user_details in users_details]
    return jsonify({'users_details': user_details_list})

@user_details_bp.route('/<int:user_id>', methods=['GET'])
def get_user_details_by_id(user_id):
    from my_project.auth.service.user_details_service import UserDetailsService
    user_details = UserDetailsService.get_user_details_by_id(user_id)
    if user_details:
        return jsonify(user_details.transform_to_json())
    else:
        return jsonify({'message': 'User not found'}), 404

@user_details_bp.route('', methods=['POST'])
def create_user_details():
    from my_project.auth.service.user_details_service import UserDetailsService
    data = request.json
    id = data.get('id')
    full_name = data.get('full_name')
    bio = data.get('bio')
    profile_picture = data.get('profile_picture')
    new_user_details = UserDetailsService.create_user_details(data)
    return jsonify(new_user_details), 201

@user_details_bp.route('/<int:user_id>', methods=['PUT'])
def update_user_details(user_id):
    from my_project.auth.service.user_details_service import UserDetailsService
    user_details = UserDetailsService.get_user_details_by_id(user_id)
    if not user_details:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    UserDetailsService.update_user_details(user_id, data)
    return jsonify({'message': 'User updated successfully'}), 200

@user_details_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user_details(user_id):
    from my_project.auth.service.user_details_service import UserDetailsService
    user_details = UserDetailsService.get_user_details_by_id(user_id)
    if not user_details:
        return jsonify({'message': 'User not found'}), 404

    UserDetailsService.delete_user_details(user_id)
    return jsonify({'message': 'User deleted successfully'}), 200
