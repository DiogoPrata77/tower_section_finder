from flask import Flask
from app.database import *
import os

app = Flask(__name__)


def create_app():
 
    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ["DB_PATH"] + 'tower_sections.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Import blueprints
    from app.views import tower_section_bp

    # Register blueprints
    app.register_blueprint(tower_section_bp)

    return app

# Create the database file and tables if it doesn't exist
if __name__ == '__main__':
    app = create_app()

   
    with app.app_context():
        init_db()

    app.run()
