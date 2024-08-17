import pytest

from src.utils.data_generators.pet_generator import FakePetFactory
from src.utils.schemes.pet_schemes import PetScheme
from src.utils.schemes.base import MessageScheme
from http import HTTPStatus
from src.enums.statuses import Statuses


def test_create_pet(pet_store_api_client):
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


def test_get_pet(
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
def test_find_by_status(
    pet_store_api_client,
    status,
):
    response = pet_store_api_client.find_by_status(status=status)
    response_json = response.json()
    all_pets_in_status = [PetScheme.model_validate(pet) for pet in response_json]
    assert response.status_code == HTTPStatus.OK
    assert all(pet.status == status for pet in all_pets_in_status)


def test_delete_pet(
    pet_store_api_client,
    created_pet,
):
    response = pet_store_api_client.delete_pet(id=created_pet.id)
    response_json = response.json()
    assert response.status_code == HTTPStatus.OK
    response_message = MessageScheme.model_validate(response_json)
    assert response_message.message == str(created_pet.id)
    assert response_message.code == HTTPStatus.OK


def test_delete_nonexistent_pet(
    pet_store_api_client,
    created_pet,
):
    pet_store_api_client.delete_pet(id=created_pet.id)
    response = pet_store_api_client.delete_pet(id=created_pet.id)
    assert response.status_code == HTTPStatus.NOT_FOUND


# def test_update_pet(
#         pet_store_api_client,
#         created_pet,
# ):
#     new_pet = FakePetFactory.build()
#     new_pet.id = created_pet.id
#
#     updated_pet_response = pet_store_api_client.update_pet(
#         id=new_pet.id,
#         category=new_pet.category,
#         name=new_pet.name,
#         photo_urls=new_pet.photo_urls,
#         status=new_pet.status,
#         tags=new_pet.tags,
#     )
#     assert updated_pet_response.status_code == HTTPStatus.OK
#
#     response_json = updated_pet_response.json()
#     updated_pet = PetScheme.model_validate(response_json)
#
#     assert new_pet == updated_pet
