"""Initialize Flask Application."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__)

    with app.app_context():
        from . import routes

        return app