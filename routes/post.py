from flask import Blueprint, request

post_pages = Blueprint("post", __name__)

@post_pages.get("/post/<string:title>")
def display_post(title: str):
    return "Display post pages"

@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        pass
    return "Create post page."