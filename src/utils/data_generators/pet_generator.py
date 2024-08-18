from dataclasses import dataclass
import random

from faker import Faker
from polyfactory.factories import DataclassFactory
from src.enums.statuses import Statuses


@dataclass
class FakeCategory:
    id: int
    name: str


@dataclass
class FakeTags:
    id: int
    name: str


@dataclass
class FakePet:
    id: int
    category: FakeCategory
    name: str
    status: str
    photo_urls: list[str]
    tags: list[FakeTags]


class FakeCategoryFactory(DataclassFactory[FakeCategory]):
    __faker__ = Faker(locale="ru_RU")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.word()


class FakeTagsFactory(DataclassFactory[FakeCategory]):
    __faker__ = Faker(locale="ru_RU")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.word()


class FakePetFactory(DataclassFactory[FakePet]):
    __faker__ = Faker(locale="ru_RU")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.word()

    @classmethod
    def status(cls) -> str:
        return random.choice([status for status in Statuses])

    @classmethod
    def category(cls) -> dict:
        category = FakeCategoryFactory.build()
        return {
            "id": category.id,
            "name": category.name,
        }

    @classmethod
    def photo_urls(cls) -> list[str]:
        return [cls.__faker__.image_url()]

    @classmethod
    def tags(cls) -> list[dict]:
        tag = FakeTagsFactory.build()
        return [
            {
                "id": tag.id,
                "name": tag.name,
            }
        ]
