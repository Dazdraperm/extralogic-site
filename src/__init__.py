from flask import Flask

from src.config import DevConfig


def create_app():
    """Create and config app"""

    app = Flask(__name__)

    # Set config from object
    app.config.from_object(DevConfig)

    # Register blueprints
    from .views import form
    app.register_blueprint(form.bp)

    return app
