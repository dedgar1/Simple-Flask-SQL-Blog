
from models.post import Post
from models.PostRepository import PostRepository
from dataclasses import dataclass


class InMemoryPostRepository(PostRepository):
    posts = []

    def __init__(self) -> None:
        super().__init__()

    def add(self, post: Post):
        self.posts.append(post)

    def get_post_by_title(self, title: str):
        for post in self.posts:
            if post.title == title:
                return post
        return ""

    def get_posts(self) -> [Post]:
        return self.posts
