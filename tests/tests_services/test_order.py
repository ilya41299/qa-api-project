from src.utils.data_generators.order_generator import FakeCategoryFactory
import pytest
from src.enums.statuses import Statuses
from http import HTTPStatus
from src.utils.schemes.order_schemes import OrderScheme


@pytest.mark.parametrize(
    "status",
    [status for status in Statuses],
)
@pytest.mark.parametrize(
    "complete",
    [True, False],
)
def test_create_order(
    pet_store_api_client,
    status,
    complete,
):
    fake_order = FakeCategoryFactory.build()
    fake_order.status = status
    fake_order.complete = complete

    response = pet_store_api_client.create_order(
        id=fake_order.id,
        pet_id=fake_order.pet_id,
        quantity=fake_order.quantity,
        ship_date=fake_order.ship_date,
        status=fake_order.status,
        complete=fake_order.complete,
    )

    assert response.status_code == HTTPStatus.OK, response.json()
    response_json = response.json()
    order = OrderScheme.model_validate(response_json)
    assert fake_order.status == order.status
    assert fake_order.complete == order.complete


def test_get_order(
    pet_store_api_client,
):
    fake_order = FakeCategoryFactory.build()

    pet_store_api_client.create_order(
        id=fake_order.id,
        pet_id=fake_order.pet_id,
        quantity=fake_order.quantity,
        ship_date=fake_order.ship_date,
        status=fake_order.status,
        complete=fake_order.complete,
    )

    response = pet_store_api_client.get_order(fake_order.id)
    assert response.status_code == HTTPStatus.OK, response.json()
    response_json = response.json()
    order = OrderScheme.model_validate(response_json)
    assert fake_order.pet_id == order.pet_id
    assert fake_order.pet_id == order.pet_id
    assert fake_order.quantity == order.quantity
    assert fake_order.status == order.status
    assert fake_order.complete == order.complete
