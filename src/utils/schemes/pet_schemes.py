from .base import BaseScheme


class TagScheme(BaseScheme):
    id: int
    name: str


class CategoryScheme(BaseScheme):
    id: int
    name: str


class PetScheme(BaseScheme):
    id: int
    category: CategoryScheme | None
    name: str
    status: str
    photo_urls: list[str]
    tags: list[TagScheme]
