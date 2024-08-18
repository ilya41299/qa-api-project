from src.utils.data_generators.user_generator import FakeUserFactory
from src.utils.schemes.base import MessageScheme
from http import HTTPStatus

from src.utils.schemes.user_schemes import UserScheme
import allure


@allure.epic("User")
class TestUsers:
    @allure.title("Create user")
    def test_create_user(
        self,
        pet_store_api_client,
    ):
        fake_user = FakeUserFactory.build()

        response = pet_store_api_client.create_user(
            id=fake_user.id,
            username=fake_user.username,
            first_name=fake_user.first_name,
            last_name=fake_user.last_name,
            email=fake_user.email,
            password=fake_user.password,
            phone=fake_user.phone,
            user_status=fake_user.user_status,
        )

        response_json = response.json()
        assert response.status_code == HTTPStatus.OK, response_json
        response_json = response.json()
        message = MessageScheme.model_validate(response_json)
        assert message.code == HTTPStatus.OK
        assert message.message == str(fake_user.id)

    @allure.title("Get user by username")
    def test_get_user(
        self,
        pet_store_api_client,
        created_user,
    ):
        response = pet_store_api_client.get_user(
            username=created_user.username,
        )

        response_json = response.json()
        assert response.status_code == HTTPStatus.OK, response_json
        received_user = UserScheme.model_validate(response_json)
        assert received_user.model_dump() == created_user.__dict__

    @allure.title("Delete user by username")
    def test_delete_user(
        self,
        pet_store_api_client,
        created_user,
    ):
        pet_store_api_client.delete_user(username=created_user.username)
        response = pet_store_api_client.logout()
        response_json = response.json()
        assert response.status_code == HTTPStatus.OK, response_json
        message = MessageScheme.model_validate(response_json)
        assert message.code == HTTPStatus.OK
        assert message.message == "ok"

    @allure.title("Delete nonexistent user")
    def test_delete_nonexistent_user(
        self,
        pet_store_api_client,
        created_user,
    ):
        pet_store_api_client.delete_user(username=created_user.username)
        response = pet_store_api_client.delete_user(username=created_user.username)
        assert response.status_code == HTTPStatus.NOT_FOUND

    @allure.title("Login")
    def test_login(
        self,
        pet_store_api_client,
        created_user,
    ):
        response = pet_store_api_client.login(
            username=created_user.username,
            password=created_user.password,
        )

        response_json = response.json()
        assert response.status_code == HTTPStatus.OK, response_json
        message = MessageScheme.model_validate(response_json)
        assert message.code == HTTPStatus.OK
        assert "logged in user session" in message.message

    @allure.title("Logout")
    def test_logout(
        self,
        pet_store_api_client,
        created_user,
    ):
        pet_store_api_client.login(
            username=created_user.username,
            password=created_user.password,
        )
        response = pet_store_api_client.logout()
        response_json = response.json()
        assert response.status_code == HTTPStatus.OK, response_json
        message = MessageScheme.model_validate(response_json)
        assert message.code == HTTPStatus.OK
        assert message.message == "ok"
