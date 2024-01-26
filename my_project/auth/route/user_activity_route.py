# app/my_project/auth/route/user_activity_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.user_activity_service import UserActivityService

user_activity_bp = Blueprint('user_activity', __name__, url_prefix='/user_activity')

@user_activity_bp.route('', methods=['GET'])
def get_all_users_user_activitys():
    from my_project.auth.service.user_activity_service import UserActivityService
    users_user_activitys = UserActivityService.get_all_users_user_activitys()
    users_user_activitys_list = [user_user_activitys.transform_to_json() for user_user_activitys in users_user_activitys]
    return jsonify({'users_user_activitys': users_user_activitys_list})

@user_activity_bp.route('/<int:user_id>', methods=['GET'])
def get_user_user_activitys_by_user_id(user_id):
    from my_project.auth.service.user_activity_service import UserActivityService
    user_user_activitys = UserActivityService.get_user_user_activitys_by_user_id(user_id)
    if user_user_activitys:
        return jsonify([user_user_activity.transform_to_json() for user_user_activity in user_user_activitys])
    else:
        return jsonify({'message': 'UserActivitys not found'}), 404

@user_activity_bp.route('/<int:user_id>/<int:user_activity_id>', methods=['GET'])
def get_user_user_activity_by_id(user_id, user_activity_id):
    from my_project.auth.service.user_activity_service import UserActivityService
    user_user_activity = UserActivityService.get_user_user_activity_by_id(user_activity_id)
    if user_user_activity and user_user_activity.user_id == user_id:
        return jsonify(user_user_activity.transform_to_json())
    else:
        return jsonify({'message': 'UserActivity not found'}), 404

@user_activity_bp.route('', methods=['POST'])
def create_user_activity():
    from my_project.auth.service.user_activity_service import UserActivityService
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    date_start = data.get('date_start')
    new_user_activity = UserActivityService.create_user_activity(data)
    return jsonify(new_user_activity), 201

@user_activity_bp.route('/<int:user_id>/<int:user_activity_id>', methods=['PUT'])
def update_user_user_activity(user_id, user_activity_id):
    from my_project.auth.service.user_activity_service import UserActivityService
    user_user_activity = UserActivityService.get_user_user_activity_by_id(user_activity_id)
    if not user_user_activity or user_user_activity.user_id != user_id:
        return jsonify({'message': 'UserActivity not found'}), 404

    data = request.json
    UserActivityService.update_user_user_activity(user_activity_id, data)
    return jsonify({'message': 'UserActivity updated successfully'}), 200

@user_activity_bp.route('/<int:user_id>/<int:user_activity_id>', methods=['DELETE'])
def delete_user_user_activity(user_id, user_activity_id):
    from my_project.auth.service.user_activity_service import UserActivityService
    user_user_activity = UserActivityService.get_user_user_activity_by_id(user_activity_id)
    if not user_user_activity or user_user_activity.user_id != user_id:
        return jsonify({'message': 'UserActivity not found'}), 404

    UserActivityService.delete_user_user_activity(user_activity_id)
    return jsonify({'message': 'UserActivity deleted successfully'}), 200