import requests
import allure
from api_testing.data import (base_url, order_endpoint)

class OrderMethods:
    @allure.step('Создание заказа через POST-запрос.')
    def create_order(self, payload):
        response = requests.post(f"{base_url}{order_endpoint}", json = payload)
        return response

    @allure.step('Получение списка заказов через GET-запрос.')
    def get_order_list(self):
        response = requests.get(f"{base_url}{order_endpoint}")
        return response

