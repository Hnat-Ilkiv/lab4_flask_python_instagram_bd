# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

# Database

db = SQLAlchemy()
print(db.__dict__, 1)
# app = Flask(__name__)
def create_app() -> Flask:
    with open('config/app.yml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Параметри підключення до бази даних
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{config['database']['user']}:{config['database']['password']}@{config['database']['host']}/{config['database']['db']}?charset=utf8"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    _init_db(app)
    from my_project.auth.route.user_route import user_bp
    app.register_blueprint(user_bp)

    from my_project.auth.route.user_details_route import user_details_bp
    app.register_blueprint(user_details_bp)

    from my_project.auth.route.post_route import post_bp
    app.register_blueprint(post_bp)

    from my_project.auth.route.story_route import story_bp
    app.register_blueprint(story_bp)

    from my_project.auth.route.comment_route import comment_bp
    app.register_blueprint(comment_bp)

    from my_project.auth.route.reaction_route import reaction_bp
    app.register_blueprint(reaction_bp)

    from my_project.auth.route.follower_route import follower_bp
    app.register_blueprint(follower_bp)

    from my_project.auth.route.message_route import message_bp
    app.register_blueprint(message_bp)

    from my_project.auth.route.chat_route import chat_bp
    app.register_blueprint(chat_bp)

    from my_project.auth.route.chat_member_route import chat_member_bp
    app.register_blueprint(chat_member_bp)

    from my_project.auth.route.chat_message_route import chat_message_bp
    app.register_blueprint(chat_message_bp)

    return app


def _init_db(app: Flask) -> None:
    db.init_app(app)
    # print("db work dto")
    from my_project.auth.models.user_model import User
    from my_project.auth.models.user_details_model import UserDetails

    with app.app_context():
        db.create_all()
        print(db.__dict__, 2)

if __name__ == '__main__':
    create_app().run(debug=True)
