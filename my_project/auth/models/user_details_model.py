# app/my_project/auth/models/model.py
from app import db

class UserDetails(db.Model):
    __tablename__ = 'user_details'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    full_name = db.Column(db.String(100))
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(255))

    # user = db.relationship('User', backref=db.backref('details_user', uselist=False), foreign_keys=[id], post_update=True)

    @staticmethod
    def transform_from_json(json):
        return UserDetails(id = json.get("id"), full_name = json.get("full_name"), bio = json.get("bio"), profile_picture = json.get("profile_picture"))

    def transform_to_json(self):
        return {'id': self.id, 'full_name': self.full_name, 'bio': self.bio, 'profile_picture': self.profile_picture}
