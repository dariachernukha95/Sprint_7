import pytest
import allure
from api_testing.methods.courier_methods import CourierMethods
from api_testing.helpers import (generate_full_data_for_courier_creation, generate_data_for_courier_creation_without_login,
                              generate_data_for_courier_creation_without_password, generate_data_for_courier_creation_without_firstname)

class TestCourierCreation:

    @allure.title('Проверки возможности создания курьера.')
    @pytest.mark.parametrize('payload',
                            [generate_full_data_for_courier_creation(), generate_data_for_courier_creation_without_firstname()])
    def test_success_courier_creation(self, payload):
        courier_methods = CourierMethods()
        response = courier_methods.create_courier(payload)
        assert response.status_code == 201 and response.json() == {"ok":True}

    @allure.title('Проверки на отображение ошибки создания курьера при незаполнении одного из обязательных полей (логин/пароль).')
    @pytest.mark.parametrize('payload',
                             [generate_data_for_courier_creation_without_login(), generate_data_for_courier_creation_without_password()])
    def test_courier_creation_without_login_or_password(self, payload):
        courier_methods = CourierMethods()
        response = courier_methods.create_courier(payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка невозможности создания двух курьеров с одинаковыми параметрами.')
    def test_creation_of_two_same_couriers(self):
        courier_methods = CourierMethods()
        payload = generate_full_data_for_courier_creation()
        courier_methods.create_courier(payload)
        response = courier_methods.create_courier(payload)
        assert response.status_code == 409 and "Этот логин уже используется" in response.json()["message"]

    @allure.title('Проверка невозможности создания курьера с уже существующим в системе логином.')
    def test_courier_creation_with_existed_login(self):
        courier_methods = CourierMethods()
        data_for_first_courier = generate_full_data_for_courier_creation()
        courier_methods.create_courier(data_for_first_courier)
        data_for_second_courier = generate_full_data_for_courier_creation()
        data_for_second_courier['login'] = data_for_first_courier['login']
        response = courier_methods.create_courier(data_for_second_courier)
        assert response.status_code == 409 and "Этот логин уже используется" in response.json()["message"]
