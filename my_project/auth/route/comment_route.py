# app/my_project/auth/route/comment_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.comment_service import CommentService

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

@comment_bp.route('', methods=['GET'])
def get_all_users_comments():
    from my_project.auth.service.comment_service import CommentService
    users_comments = CommentService.get_all_users_comments()
    users_comments_list = [user_comments.transform_to_json() for user_comments in users_comments]
    return jsonify({'users_comments': users_comments_list})

@comment_bp.route('/post/<int:post_id>', methods=['GET'])
def get_comments_by_post_id(post_id):
    from my_project.auth.service.comment_service import CommentService
    user_comments = CommentService.get_comments_by_post_id(post_id)
    if user_comments:
        return jsonify([user_comment.transform_to_json() for user_comment in user_comments])
    else:
        return jsonify({'message': 'Comments not found'}), 404

@comment_bp.route('/story/<int:story_id>', methods=['GET'])
def get_comments_by_story_id(story_id):
    from my_project.auth.service.comment_service import CommentService
    user_comments = CommentService.get_comments_by_story_id(story_id)
    if user_comments:
        return jsonify([user_comment.transform_to_json() for user_comment in user_comments])
    else:
        return jsonify({'message': 'Comments not found'}), 404

@comment_bp.route('/one/<int:comment_id>', methods=['GET'])
def get_comment_by_id(comment_id):
    from my_project.auth.service.comment_service import CommentService
    user_comment = CommentService.get_comment_by_id(comment_id)
    if user_comment:
        return jsonify(user_comment.transform_to_json())
    else:
        return jsonify({'message': 'Comment not found'}), 404

@comment_bp.route('', methods=['POST'])
def create_comment():
    from my_project.auth.service.comment_service import CommentService
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    post_id = data.get('post_id')
    story_id = data.get('story_id')
    text = data.get('text')
    new_comment = CommentService.create_comment(data)
    return jsonify(new_comment), 201

@comment_bp.route('/one/<int:comment_id>', methods=['PUT'])
def update_user_comment(comment_id):
    from my_project.auth.service.comment_service import CommentService
    user_comment = CommentService.get_user_comment_by_id(comment_id)
    if not user_comment:
        return jsonify({'message': 'Comment not found'}), 404

    data = request.json
    CommentService.update_user_comment(comment_id, data)
    return jsonify({'message': 'Comment updated successfully'}), 200

@comment_bp.route('/one/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    from my_project.auth.service.comment_service import CommentService
    user_comment = CommentService.get_user_comment_by_id(comment_id)
    if not user_comment:
        return jsonify({'message': 'Comment not found'}), 404

    CommentService.delete_comment(comment_id)
    return jsonify({'message': 'Comment deleted successfully'}), 200