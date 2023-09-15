from flask import Flask
from routes.post import post_pages

def create_app():
    app = Flask(__name__)
    app.register_blueprint(post_pages)
    return app