import allure
from api_testing.methods.order_methods import OrderMethods

class TestOrderListReceiving:

    @allure.title('Проверка получения списка заказов.')
    def test_order_list_receiving(self):
        order_methods = OrderMethods()
        response = order_methods.get_order_list()
        assert response.status_code == 200 and response.json()["orders"] is not None
