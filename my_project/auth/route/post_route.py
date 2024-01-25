# app/my_project/auth/route/post_route.py
from flask import Blueprint, jsonify, request
# from my_project.auth.service.post_service import PostService

post_bp = Blueprint('post', __name__, url_prefix='/post')

@post_bp.route('', methods=['GET'])
def get_all_users_posts():
    from my_project.auth.service.post_service import PostService
    users_posts = PostService.get_all_users_posts()
    users_posts_list = [user_posts.transform_to_json() for user_posts in users_posts]
    return jsonify({'users_posts': users_posts_list})

@post_bp.route('/<int:user_id>', methods=['GET'])
def get_user_posts_by_user_id(user_id):
    from my_project.auth.service.post_service import PostService
    user_posts = PostService.get_user_posts_by_user_id(user_id)
    if user_posts:
        return jsonify([user_post.transform_to_json() for user_post in user_posts])
    else:
        return jsonify({'message': 'Posts not found'}), 404

@post_bp.route('/<int:user_id>/<int:post_id>', methods=['GET'])
def get_user_post_by_id(user_id, post_id):
    from my_project.auth.service.post_service import PostService
    user_post = PostService.get_user_post_by_id(post_id)
    if user_post and user_post.user_id == user_id:
        return jsonify(user_post.transform_to_json())
    else:
        return jsonify({'message': 'Post not found'}), 404

@post_bp.route('', methods=['POST'])
def create_post():
    from my_project.auth.service.post_service import PostService
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    caption = data.get('caption')
    image_url = data.get('image_url')
    new_post = PostService.create_post(data)
    return jsonify(new_post), 201

@post_bp.route('/<int:user_id>/<int:post_id>', methods=['PUT'])
def update_user_post(user_id, post_id):
    from my_project.auth.service.post_service import PostService
    user_post = PostService.get_user_post_by_id(post_id)
    if not user_post or user_post.user_id != user_id:
        return jsonify({'message': 'Post not found'}), 404

    data = request.json
    PostService.update_user_post(post_id, data)
    return jsonify({'message': 'Post updated successfully'}), 200

@post_bp.route('/<int:user_id>/<int:post_id>', methods=['DELETE'])
def delete_user_post(user_id, post_id):
    from my_project.auth.service.post_service import PostService
    user_post = PostService.get_user_post_by_id(post_id)
    if not user_post or user_post.user_id != user_id:
        return jsonify({'message': 'Post not found'}), 404

    PostService.delete_user_post(post_id)
    return jsonify({'message': 'Post deleted successfully'}), 200