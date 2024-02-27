"""Initialize Flask Application."""
from flask import Flask


def create_app() -> Flask:
    """Construct the core application."""
    app = Flask(__name__)

    with app.app_context():
        from . import routes  # noqa: F401

        return app
