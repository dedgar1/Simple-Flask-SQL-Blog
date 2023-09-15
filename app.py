from flask import Flask, app
from routes.post import post_pages
from sqlmodel import SQLModel, create_engine
from models.post import Post

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.engine = create_engine("sqlite:///database.db")

    with app.app_context():
        # before_first_request equivalent here
        SQLModel.metadata.create_all(app.engine)

        # Register Blueprints
        app.register_blueprint(post_pages)
        return app



if __name__ == "__main__":
    app = init_app()
    app.run(host='0.0.0.0', port=5001)