import allure
from faker import Faker
from api_testing.methods.courier_methods import CourierMethods

#Генерация данных для создания курьера
def generate_courier_login():
    faker = Faker()
    login = faker.user_name()
    return login

def generate_courier_password():
    faker = Faker()
    password = faker.password()
    return password

def generate_courier_firstname():
    faker = Faker()
    firstname = faker.first_name()
    return firstname

@allure.step('Генерация тела запроса со всеми параметрами для создания курьера.')
def generate_full_data_for_courier_creation():
    payload = {
        "login": generate_courier_login(),
        "password": generate_courier_password(),
        "firstName": generate_courier_firstname()
    }
    return payload

@allure.step('Генерация тела запроса для создания курьера без поля login.')
def generate_data_for_courier_creation_without_login():
    payload = {
        "password": generate_courier_password(),
        "firstName": generate_courier_firstname()
    }
    return payload

@allure.step('Генерация тела запроса для создания курьера без поля password.')
def generate_data_for_courier_creation_without_password():
    payload = {
        "login": generate_courier_login(),
        "firstName": generate_courier_firstname()
    }
    return payload

@allure.step('Генерация тела запроса для создания курьера без поля firstname.')
def generate_data_for_courier_creation_without_firstname():
    payload = {
        "login": generate_courier_login(),
        "password": generate_courier_password()
    }
    return payload

@allure.step('Регистрация курьера и сохранение его логина и пароля.')
def register_new_courier_and_return_login_password():
    login_pass = {}
    login = generate_courier_login()
    password = generate_courier_password()
    first_name = generate_courier_firstname()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    courier_methods = CourierMethods()
    response = courier_methods.create_courier(payload)
    if response.status_code == 201:
        login_pass["login"] = login
        login_pass["password"] = password
    return login_pass