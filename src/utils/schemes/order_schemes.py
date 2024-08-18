from .base import BaseScheme


class OrderScheme(BaseScheme):
    id: int
    pet_id: int
    quantity: int
    ship_date: str
    status: str
    complete: bool
