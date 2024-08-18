import pytest
from src.utils.api.api_client_petstore import PetStoreApiClient
from src.utils.data_generators.pet_generator import FakePetFactory
from src.utils.data_generators.user_generator import FakeUserFactory, FakeUser
from src.utils.schemes.pet_schemes import PetScheme


@pytest.fixture(scope="session")
def pet_store_api_client():
    return PetStoreApiClient()


@pytest.fixture(scope="function")
def created_pet(pet_store_api_client) -> PetScheme:
    fake_pet = FakePetFactory.build()
    response = pet_store_api_client.create_pet(
        id=fake_pet.id,
        category=fake_pet.category,
        name=fake_pet.name,
        photo_urls=fake_pet.photo_urls,
        status=fake_pet.status,
        tags=fake_pet.tags,
    )
    return PetScheme.model_validate(response.json())


@pytest.fixture(scope="function")
def created_user(pet_store_api_client) -> FakeUser:
    fake_user = FakeUserFactory.build()
    pet_store_api_client.create_user(
        id=fake_user.id,
        username=fake_user.username,
        first_name=fake_user.first_name,
        last_name=fake_user.last_name,
        email=fake_user.email,
        password=fake_user.password,
        phone=fake_user.phone,
        user_status=fake_user.user_status,
    )

    return fake_user
