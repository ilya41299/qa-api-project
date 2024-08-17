from dataclasses import dataclass
import random
from src.enums.statuses import Statuses
from faker import Faker
from polyfactory.factories import DataclassFactory


@dataclass
class FakeOrder:
    id: int
    pet_id: int
    quantity: int
    ship_date: str
    status: str
    complete: bool


class FakeCategoryFactory(DataclassFactory[FakeOrder]):
    __faker__ = Faker(locale="ru_RU")

    @classmethod
    def name(cls) -> str:
        return cls.__faker__.word()

    @classmethod
    def ship_date(cls) -> str:
        return cls.__faker__.date_time().isoformat()

    @classmethod
    def status(cls) -> str:
        return random.choice([status for status in Statuses])

    @classmethod
    def complete(cls) -> bool:
        return cls.__faker__.boolean(chance_of_getting_true=50)
