from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    director = db.Column(db.String(128), nullable=False)
    release_date = db.Column(db.String(128), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'release_date': self.release_date
        }

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)