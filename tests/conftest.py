import pytest
import requests
from selenium import webdriver
from pages.auth_page import AuthPage
from data.urls import Urls
from helpers.helpers import generate_user_data

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = generate_user_data()
    response = requests.post(Urls.REGISTER_USER_URL, json=user_data)
    token = response.json()["accessToken"]
    user_data["token"] = f"Bearer {token}"
    yield user_data
    requests.delete(Urls.USER_URL, headers={"Authorization": user_data["token"]})

@pytest.fixture(scope="function")
def login_user(driver, create_and_delete_user):
    auth_page = AuthPage(driver)
    auth_page.open_auth_page()
    auth_page.auth(create_and_delete_user["email"], create_and_delete_user["password"])
    return driver


