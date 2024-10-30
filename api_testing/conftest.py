import pytest
from api_testing.helpers import register_new_courier_and_return_login_password,generate_full_data_for_courier_creation
from api_testing.methods.courier_methods import CourierMethods

@pytest.fixture
def login_pass():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass
    print(login_pass)
    courier_methods = CourierMethods()
    response = courier_methods.courier_login(login_pass)
    id = response.json()["id"]
    courier_methods.delete_courier(id)
