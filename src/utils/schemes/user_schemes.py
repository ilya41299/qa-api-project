from .base import BaseScheme


class UserScheme(BaseScheme):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    user_status: int
