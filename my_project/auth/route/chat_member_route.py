# app/my_project/auth/route/chat_member_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.chat_member_service import ChatMemberService

chat_member_bp = Blueprint('chat_member', __name__, '')

@chat_member_bp.route('/user_chats/<int:user_id>', methods=['GET'])
def get_user_chats(user_id):
    from my_project.auth.service.chat_member_service import ChatMemberService
    user_chat_members = ChatMemberService.get_user_chats(user_id)
    if user_chat_members:
        return jsonify([user_chat_member.transform_to_json() for user_chat_member in user_chat_members])
    else:
        return jsonify({'chat_member': 'ChatMembers not found'}), 404

@chat_member_bp.route('/user_in_chat/<int:chat_id>', methods=['GET'])
def get_user_in_chat(chat_id):
    from my_project.auth.service.chat_member_service import ChatMemberService
    user_chat_members = ChatMemberService.get_user_in_chat(chat_id)
    if user_chat_members:
        return jsonify([user_chat_member.transform_to_json() for user_chat_member in user_chat_members])
    else:
        return jsonify({'chat_member': 'ChatMembers not found'}), 404

@chat_member_bp.route('/chat_member/<int:chat_member_id>', methods=['GET'])
def get_chat_member_by_id(chat_member_id):
    from my_project.auth.service.chat_member_service import ChatMemberService
    user_chat_member = ChatMemberService.get_chat_member_by_id(chat_member_id)
    if user_chat_member:
        return jsonify(user_chat_member.transform_to_json())
    else:
        return jsonify({'chat_member': 'ChatMember not found'}), 404

@chat_member_bp.route('/chat_member', methods=['POST'])
def create_chat_member():
    from my_project.auth.service.chat_member_service import ChatMemberService
    data = request.json
    id = data.get('id')
    chat_id = data.get('chat_id')
    user_id = data.get('user_id')
    new_chat_member = ChatMemberService.create_chat_member(data)
    return jsonify(new_chat_member), 201

@chat_member_bp.route('/chat_member/<int:chat_member_id>', methods=['PUT'])
def update_chat_member(chat_member_id):
    from my_project.auth.service.chat_member_service import ChatMemberService
    user_chat_member = ChatMemberService.get_chat_member_by_id(chat_member_id)
    if not user_chat_member:
        return jsonify({'chat_member': 'ChatMember not found'}), 404

    data = request.json
    ChatMemberService.update_chat_member(chat_member_id, data)
    return jsonify({'chat_member': 'ChatMember updated successfully'}), 200

@chat_member_bp.route('/chat_member/<int:chat_member_id>', methods=['DELETE'])
def delete_chat_member(chat_member_id):
    from my_project.auth.service.chat_member_service import ChatMemberService
    user_chat_member = ChatMemberService.get_chat_member_by_id(chat_member_id)
    if not user_chat_member:
        return jsonify({'chat_member': 'ChatMember not found'}), 404

    ChatMemberService.delete_chat_member(chat_member_id)
    return jsonify({'chat_member': 'ChatMember deleted successfully'}), 200