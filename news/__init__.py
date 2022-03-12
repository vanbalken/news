from flask import Flask
from flask_migrate import Migrate
from .models import db


migrate = Migrate()


def create_app():
    """Create and configure the app."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:docker@localhost/postgres"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)       

        from . import routes

        return app