from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from random import randint


@dataclass
class Post():
    title: str
    content: str
    publish_date: datetime
    id: Optional[int] = randint(0, 1000)
