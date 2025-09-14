import allure
from pages.base_page import BasePage
from locators.locators import PersonalAccountLocators
from locators.locators import MainPageLocators
from data.urls import Urls


class AuthPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_auth_page(self):
        self.open_page(Urls.LOGIN)

    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.send_keys_to_field(PersonalAccountLocators.EMAIL, email)
        self.send_keys_to_field(PersonalAccountLocators.PASSWORD, password)
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.click_on_element(PersonalAccountLocators.LOGIN_BUTTON)
