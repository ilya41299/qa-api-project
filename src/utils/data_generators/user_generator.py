from pydantic import dataclasses

from faker import Faker
from polyfactory.factories import DataclassFactory


@dataclasses.dataclass
class FakeUser:
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    user_status: int


class FakeUserFactory(DataclassFactory[FakeUser]):
    __faker__ = Faker(locale="ru_RU")

    @classmethod
    def username(cls) -> str:
        return cls.__faker__.user_name()

    @classmethod
    def first_name(cls) -> str:
        return cls.__faker__.first_name()

    @classmethod
    def last_name(cls) -> str:
        return cls.__faker__.last_name()

    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()

    @classmethod
    def password(cls) -> str:
        return cls.__faker__.password()

    @classmethod
    def phone(cls) -> str:
        return cls.__faker__.phone_number()
