import pytest
import allure
from api_testing.methods.order_methods import OrderMethods
from api_testing.data import data_for_order_creation

class TestOrderCreation:

    @pytest.mark.parametrize('color',
                             [
                              ["BLACK"],
                              ["BLACK", "GREY"],
                              ["GREY"],
                              []
                             ])
    @allure.title('Проверка возможности создания заказа.')
    def test_success_order_creation(self,color):
        order_methods = OrderMethods()
        payload = data_for_order_creation
        payload["color"] = color
        response = order_methods.create_order(payload)
        assert response.status_code == 201 and response.json()["track"] is not None