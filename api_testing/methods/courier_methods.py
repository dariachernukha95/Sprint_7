import requests
import allure
from api_testing.data import (base_url,create_courier_endpoint,courier_login_endpoint)

class CourierMethods:

    @allure.step('Создание курьера через POST-запрос.')
    def create_courier(self, payload):
        response = requests.post(f"{base_url}{create_courier_endpoint}", data = payload)
        return response

    @allure.step('Логин курьера через POST-запрос.')
    def courier_login(self, payload):
        response = requests.post(f"{base_url}{courier_login_endpoint}", data = payload)
        return response

    @allure.step('Удаление курьера через DELETE-запрос.')
    def delete_courier(self, id):
        response = requests.delete(f"{base_url}{create_courier_endpoint}{id}")
        return response