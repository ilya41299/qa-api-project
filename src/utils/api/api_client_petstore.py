from http import HTTPMethod

import requests

from config import settings

from .api_client import HTTPClient


class PetStoreApiClient(HTTPClient):
    def __init__(self, base_url=settings.base_url):
        super().__init__(base_url=base_url)

    def get_pet(self, id: int) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.GET,
            path=f"v2/pet/{id}/",
        )

    def create_pet(
        self,
        id: int,
        category: dict,
        name: str,
        photo_urls: list[str],
        status: str,
        tags: list[str],
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.POST,
            path="v2/pet/",
            json={
                "id": id,
                "category": category,
                "name": name,
                "photoUrls": photo_urls,
                "tags": tags,
                "status": status,
            },
        )

    def find_by_status(
        self,
        status: str,
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.GET,
            path="v2/pet/findByStatus/",
            query={
                "status": status,
            },
        )

    def update_pet(
        self,
        id: int,
        category: dict,
        name: str,
        photo_urls: list[str],
        status: str,
        tags: list[str],
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.PUT,
            path=f"/v2/pet/{id}/",
            json={
                "category": category,
                "name": name,
                "photoUrls": photo_urls,
                "tags": tags,
                "status": status,
            },
        )

    def delete_pet(
        self,
        id: int,
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.DELETE,
            path=f"/v2/pet/{id}/",
            json={
                "petId": id,
            },
        )

    def create_user(
        self,
        id: int,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        phone: str,
        user_status: int,
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.POST,
            path="/v2/user/",
            json={
                "id": id,
                "username": username,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "password": password,
                "phone": phone,
                "userStatus": user_status,
            },
        )

    def delete_user(self, username: str) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.DELETE,
            path=f"/v2/user/{username}/",
        )

    def get_user(
        self,
        username: str,
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.GET,
            path=f"/v2/user/{username}",
        )

    def login(self, username: str, password: str) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.GET,
            path="/v2/user/login/",
            json={
                "username": username,
                "password": password,
            },
        )

    def logout(self) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.GET,
            path="/v2/user/logout/",
        )

    def create_order(
        self,
        id: int,
        pet_id: int,
        quantity: int,
        ship_date: str,
        status: str,
        complete: bool,
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.POST,
            path="/v2/store/order/",
            json={
                "id": id,
                "petId": pet_id,
                "quantity": quantity,
                "shipDate": ship_date,
                "status": status,
                "complete": complete,
            },
        )

    def get_order(
        self,
        id: int,
    ) -> requests.models.Response:
        return self.make_request(
            method=HTTPMethod.GET,
            path=f"/v2/store/order/{id}/",
        )

