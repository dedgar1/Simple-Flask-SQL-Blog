from flask import Blueprint, request, render_template, redirect, url_for, current_app
from sqlmodel import Session, select
from models.post import Post
from datetime import datetime
from models.inMemoryPostRepository import InMemoryPostRepository
post_pages = Blueprint("post", __name__)


@post_pages.get("/post/<string:title>")
def display_post(title: str):
    post = InMemoryPostRepository().get_post_by_title(title)
    return render_template("post.html", title=title, content=post.content)


@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post = Post(title=title, content=content, publish_date=datetime.now())
        InMemoryPostRepository().add(post)
        return redirect(url_for(".display_post", title=title))

    if request.method == "GET":
        title = "List of posts"
        posts = InMemoryPostRepository().get_posts()
        print(type(posts))
        for post in posts:
            print(post)
        return render_template("all_posts.html", page_title=title, posts=posts)
