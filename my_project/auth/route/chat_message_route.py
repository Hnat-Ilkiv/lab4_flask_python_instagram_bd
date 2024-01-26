# app/my_project/auth/route/chat_message_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.chat_message_service import ChatMessageService

chat_message_bp = Blueprint('chat_message', __name__, '')

@chat_message_bp.route('/message_chats/<int:message_id>', methods=['GET'])
def get_message_chats(message_id):
    from my_project.auth.service.chat_message_service import ChatMessageService
    user_chat_messages = ChatMessageService.get_message_chats(message_id)
    if user_chat_messages:
        return jsonify([user_chat_message.transform_to_json() for user_chat_message in user_chat_messages])
    else:
        return jsonify({'chat_message': 'ChatMessages not found'}), 404

@chat_message_bp.route('/message_in_chat/<int:chat_id>', methods=['GET'])
def get_message_in_chat(chat_id):
    from my_project.auth.service.chat_message_service import ChatMessageService
    user_chat_messages = ChatMessageService.get_message_in_chat(chat_id)
    if user_chat_messages:
        return jsonify([user_chat_message.transform_to_json() for user_chat_message in user_chat_messages])
    else:
        return jsonify({'chat_message': 'ChatMessages not found'}), 404

@chat_message_bp.route('/chat_message/<int:chat_message_id>', methods=['GET'])
def get_chat_message_by_id(chat_message_id):
    from my_project.auth.service.chat_message_service import ChatMessageService
    user_chat_message = ChatMessageService.get_chat_message_by_id(chat_message_id)
    if user_chat_message:
        return jsonify(user_chat_message.transform_to_json())
    else:
        return jsonify({'chat_message': 'ChatMessage not found'}), 404

@chat_message_bp.route('/chat_message', methods=['POST'])
def create_chat_message():
    from my_project.auth.service.chat_message_service import ChatMessageService
    data = request.json
    id = data.get('id')
    chat_id = data.get('chat_id')
    user_id = data.get('user_id')
    new_chat_message = ChatMessageService.create_chat_message(data)
    return jsonify(new_chat_message), 201

@chat_message_bp.route('/chat_message/<int:chat_message_id>', methods=['PUT'])
def update_chat_message(chat_message_id):
    from my_project.auth.service.chat_message_service import ChatMessageService
    user_chat_message = ChatMessageService.get_chat_message_by_id(chat_message_id)
    if not user_chat_message:
        return jsonify({'chat_message': 'ChatMessage not found'}), 404

    data = request.json
    ChatMessageService.update_chat_message(chat_message_id, data)
    return jsonify({'chat_message': 'ChatMessage updated successfully'}), 200

@chat_message_bp.route('/chat_message/<int:chat_message_id>', methods=['DELETE'])
def delete_chat_message(chat_message_id):
    from my_project.auth.service.chat_message_service import ChatMessageService
    user_chat_message = ChatMessageService.get_chat_message_by_id(chat_message_id)
    if not user_chat_message:
        return jsonify({'chat_message': 'ChatMessage not found'}), 404

    ChatMessageService.delete_chat_message(chat_message_id)
    return jsonify({'chat_message': 'ChatMessage deleted successfully'}), 200