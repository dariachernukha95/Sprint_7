import pytest
import allure
from api_testing.methods.courier_methods import CourierMethods
from api_testing.data import nonexistent_login_password

class TestCourierLogin:

    @allure.title('Проверка возможности авторизации курьера.')
    def test_success_courier_authorization(self, login_pass):
        courier_methods = CourierMethods()
        payload = login_pass
        response = courier_methods.courier_login(payload)
        assert response.status_code == 200 and response.json()["id"] is not None

    @allure.title('Проверка на отображение ошибки при попытке авторизации без логина.')
    def test_courier_authorization_without_login(self, login_pass):
        courier_methods = CourierMethods()
        payload = {
                   "password": login_pass["password"]
                   }
        response = courier_methods.courier_login(payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"
    #
    @allure.title('Проверка на отображение ошибки при попытке авторизации без пароля.')
    def test_courier_authorization_without_password(self, login_pass):
        courier_methods = CourierMethods()
        payload = {"login": login_pass["login"]
                   }
        response = courier_methods.courier_login(payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка на отображение ошибки при попытке авторизации под несуществующим пользователем.')
    def test_courier_authorization_with_nonexistent_login(self):
        courier_methods = CourierMethods()
        payload = nonexistent_login_password
        response = courier_methods.courier_login(payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
    #
    @allure.title('Проверка на отображение ошибки при попытке авторизации с некорректным паролем.')
    def test_courier_authorization_with_incorrect_password(self, login_pass):
        courier_methods = CourierMethods()
        payload = {"login": login_pass["login"],
                   "password": "123"
                   }
        response = courier_methods.courier_login(payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"
    #
    @allure.title('Проверка на отображение ошибки при попытке авторизации с некорректным логином.')
    def test_courier_authorization_with_incorrect_login(self, login_pass):
        courier_methods = CourierMethods()
        payload = {"login": "dariachernukha95",
                   "password": login_pass["password"]
                   }
        response = courier_methods.courier_login(payload)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"