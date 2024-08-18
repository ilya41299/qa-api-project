import allure
import pytest

from src.utils.data_generators.pet_generator import FakePetFactory
from src.utils.schemes.pet_schemes import PetScheme
from src.utils.schemes.base import MessageScheme
from http import HTTPStatus
from src.enums.statuses import Statuses


@allure.epic("Pet")
class TestPets:
    @allure.title("Create pet")
    def test_create_pet(
        self,
        pet_store_api_client,
    ):
        fake_pet = FakePetFactory.build()

        response = pet_store_api_client.create_pet(
            id=fake_pet.id,
            category=fake_pet.category,
            name=fake_pet.name,
            photo_urls=fake_pet.photo_urls,
            status=fake_pet.status,
            tags=fake_pet.tags,
        )

        response_json = response.json()
        PetScheme.model_validate(response_json)
        assert response.status_code == HTTPStatus.OK, response_json

    @allure.title("Get pet by id")
    def test_get_pet(
        self,
        pet_store_api_client,
        created_pet,
    ):
        response = pet_store_api_client.get_pet(id=created_pet.id)
        response_json = response.json()
        PetScheme.model_validate(response_json)
        assert response.status_code == HTTPStatus.OK
        assert created_pet == PetScheme.model_validate(response_json)

    @pytest.mark.parametrize(
        "status",
        [status for status in Statuses],
    )
    @allure.title("Get pets by status")
    def test_find_by_status(
        self,
        pet_store_api_client,
        status,
    ):
        response = pet_store_api_client.find_by_status(status=status)
        response_json = response.json()
        all_pets_in_status = [PetScheme.model_validate(pet) for pet in response_json]
        assert response.status_code == HTTPStatus.OK
        assert all(pet.status == status for pet in all_pets_in_status)

    @allure.title("Delete pet by id")
    def test_delete_pet(
        self,
        pet_store_api_client,
        created_pet,
    ):
        response = pet_store_api_client.delete_pet(id=created_pet.id)
        response_json = response.json()
        assert response.status_code == HTTPStatus.OK
        response_message = MessageScheme.model_validate(response_json)
        assert response_message.message == str(created_pet.id)
        assert response_message.code == HTTPStatus.OK

    @allure.title("Delete nonexistent pet")
    def test_delete_nonexistent_pet(
        self,
        pet_store_api_client,
        created_pet,
    ):
        pet_store_api_client.delete_pet(id=created_pet.id)
        response = pet_store_api_client.delete_pet(id=created_pet.id)
        assert response.status_code == HTTPStatus.NOT_FOUND
