from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from app.models import Movie, User
from app import db

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies', methods=['GET'])
@jwt_required()
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@movies_bp.route('/movies', methods=['POST'])
@jwt_required()
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
@jwt_required()
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

@movies_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400
    
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@movies_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200