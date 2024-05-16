from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure the PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wbnpedam:pmQC-VgpgbLUZm_ffX-_y75v-O15nl0J@fanny.db.elephantsql.com/wbnpedam'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes import movies_bp
    app.register_blueprint(movies_bp)
    
    return app