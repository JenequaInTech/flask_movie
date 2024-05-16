from flask import Blueprint, jsonify, request
from app.models import Movie
from app import db

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@movies_bp.route('/movies', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    new_movie = Movie(
        title=movie_data['title'],
        director=movie_data['director'],
        release_date=movie_data['release_date']
    )
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.to_dict()), 201

@movies_bp.route('/movies/<int:movie_id>', methods=['GET', 'PUT', 'DELETE'])
def movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'GET':
        return jsonify(movie.to_dict())
    elif request.method == 'PUT':
        movie_data = request.get_json()
        movie.title = movie_data['title']
        movie.director = movie_data['director']
        movie.release_date = movie_data['release_date']
        db.session.commit()
        return jsonify(movie.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie deleted'})