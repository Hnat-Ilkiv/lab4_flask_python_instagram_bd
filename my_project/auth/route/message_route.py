# app/my_project/auth/route/message_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.message_service import MessageService

message_bp = Blueprint('message', __name__, '')

@message_bp.route('/sender/<int:user_id>', methods=['GET'])
def get_sender(user_id):
    from my_project.auth.service.message_service import MessageService
    user_messages = MessageService.get_sender(user_id)
    if user_messages:
        return jsonify([user_message.transform_to_json() for user_message in user_messages])
    else:
        return jsonify({'message': 'Messages not found'}), 404

@message_bp.route('/receiver/<int:user_id>', methods=['GET'])
def get_receiver(user_id):
    from my_project.auth.service.message_service import MessageService
    user_messages = MessageService.get_receiver(user_id)
    if user_messages:
        return jsonify([user_message.transform_to_json() for user_message in user_messages])
    else:
        return jsonify({'message': 'Messages not found'}), 404

@message_bp.route('/message/<int:message_id>', methods=['GET'])
def get_message_by_id(message_id):
    from my_project.auth.service.message_service import MessageService
    user_message = MessageService.get_message_by_id(message_id)
    if user_message:
        return jsonify(user_message.transform_to_json())
    else:
        return jsonify({'message': 'Message not found'}), 404

@message_bp.route('/message', methods=['POST'])
def create_message():
    from my_project.auth.service.message_service import MessageService
    data = request.json
    id = data.get('id')
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    text = data.get('text')
    is_read = data.get('is_read')
    new_message = MessageService.create_message(data)
    return jsonify(new_message), 201

@message_bp.route('/message/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    from my_project.auth.service.message_service import MessageService
    user_message = MessageService.get_message_by_id(message_id)
    if not user_message:
        return jsonify({'message': 'Message not found'}), 404

    data = request.json
    MessageService.update_message(message_id, data)
    return jsonify({'message': 'Message updated successfully'}), 200

@message_bp.route('/message/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    from my_project.auth.service.message_service import MessageService
    user_message = MessageService.get_message_by_id(message_id)
    if not user_message:
        return jsonify({'message': 'Message not found'}), 404

    MessageService.delete_message(message_id)
    return jsonify({'message': 'Message deleted successfully'}), 200