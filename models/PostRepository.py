import abc
from models.post import Post


class PostRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, post: Post):
        raise NotImplementedError

    @abc.abstractmethod
    def get_post_by_title(self, reference) -> Post:
        raise NotImplementedError

    @abc.abstractmethod
    def get_posts(self) -> [Post]:
        raise NotImplementedError
