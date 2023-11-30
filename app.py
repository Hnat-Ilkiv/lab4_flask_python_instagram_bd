# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Завантаження конфігурації з файлу
with open('config/app.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Параметри підключення до бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{config['database']['user']}:{config['database']['password']}@{config['database']['host']}/{config['database']['db']}?charset=utf8"

db = SQLAlchemy(app)

# Додайте маршрути для користувачів
from my_project.auth.route.user_route import user_bp
app.register_blueprint(user_bp, url_prefix='/user')

# Опрацювання помилки "Working outside of application context"
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
