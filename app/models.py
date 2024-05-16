from . import db

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