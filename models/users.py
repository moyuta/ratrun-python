from api.database import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'<User {self.name}>'
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def get_id(self):
        return str(self.id)
