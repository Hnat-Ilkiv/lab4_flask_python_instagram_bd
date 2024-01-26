# app/my_project/auth/route/chat_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.chat_service import ChatService

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('', methods=['GET'])
def get_all_chats():
    from my_project.auth.service.chat_service import ChatService
    users_chats = ChatService.get_all_chats()
    users_chats_list = [user_chats.transform_to_json() for user_chats in users_chats]
    return jsonify({'users_chats': users_chats_list})

@chat_bp.route('/admin/<int:admin_id>', methods=['GET'])
def get_chats_by_admain_id(admin_id):
    from my_project.auth.service.chat_service import ChatService
    user_chats = ChatService.get_chats_by_admain_id(admin_id)
    if user_chats:
        return jsonify([user_chat.transform_to_json() for user_chat in user_chats])
    else:
        return jsonify({'message': 'Chats not found'}), 404

@chat_bp.route('/<int:chat_id>', methods=['GET'])
def get_chat_by_id(chat_id):
    from my_project.auth.service.chat_service import ChatService
    user_chat = ChatService.get_chat_by_id(chat_id)
    if user_chat:
        return jsonify(user_chat.transform_to_json())
    else:
        return jsonify({'message': 'Chat not found'}), 404

@chat_bp.route('', methods=['POST'])
def create_chat():
    from my_project.auth.service.chat_service import ChatService
    data = request.json
    id = data.get('id')
    chat_name = data.get('chat_name')
    admin_id = data.get('admin_id')
    new_chat = ChatService.create_chat(data)
    return jsonify(new_chat), 201

@chat_bp.route('/<int:chat_id>', methods=['PUT'])
def update_chat(chat_id):
    from my_project.auth.service.chat_service import ChatService
    user_chat = ChatService.get_chat_by_id(chat_id)
    if not user_chat:
        return jsonify({'message': 'Chat not found'}), 404

    data = request.json
    ChatService.update_chat(chat_id, data)
    return jsonify({'message': 'Chat updated successfully'}), 200

@chat_bp.route('/<int:chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    from my_project.auth.service.chat_service import ChatService
    user_chat = ChatService.get_chat_by_id(chat_id)
    if not user_chat:
        return jsonify({'message': 'Chat not found'}), 404

    ChatService.delete_chat(chat_id)
    return jsonify({'message': 'Chat deleted successfully'}), 200