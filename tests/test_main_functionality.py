import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.epic("Основная функциональность")
@allure.feature("Навигация и взаимодействие")
class TestMainPage:

    @allure.title("Переход по клику на Конструктор")
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открываем страницу Ленты заказов для проверки перехода"):
            order_page.open_order_page()
            main_page.wait_for_page_to_load()

        with allure.step("Кликаем на кнопку Конструктор"):
            main_page.click_on_constructor_button()

        with allure.step("Проверяем, что главная страница открыта"):
            assert main_page.is_main_page_opened()

    @allure.title("Переход по клику на Лента заказов")
    def test_click_on_feed_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
            main_page.wait_for_page_to_load()

        with allure.step("Кликаем на кнопку Лента заказов"):
            main_page.click_on_feed_button()

        with allure.step("Проверяем, что открыта страница Ленты заказов"):
            assert order_page.is_order_page_opened()

    @allure.title("Клик на ингредиент открывает модальное окно")
    def test_click_on_ingredient_opens_modal_window(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
            main_page.wait_for_page_to_load()

        with allure.step("Кликаем на ингредиент"):
            main_page.click_on_ingredient()

        with allure.step("Проверяем, что модальное окно открыто"):
            assert main_page.is_modal_visible()

    @allure.title("Модальное окно закрывается по крестику")
    def test_close_modal_window_with_close_button(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу и ждем загрузки"):
            main_page.open_main_page()
            main_page.wait_for_page_to_load()

        with allure.step("Кликаем на ингредиент и закрываем модальное окно"):
            main_page.click_on_ingredient()
            main_page.close_ingredient_modal()

        with allure.step("Проверяем, что модальное окно закрыто"):
            assert main_page.is_modal_closed()

    @allure.title("Счётчик ингредиента увеличивается при добавлении ингредиента в заказ")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу и ждем загрузки"):
            main_page.open_main_page()
            main_page.wait_for_page_to_load()

        with allure.step("Получаем текущий счётчик ингредиента"):
            original_count = main_page.get_ingredient_counter()

        with allure.step("Кликаем на ингредиент и перетаскиваем в корзину"):
            main_page.click_on_ingredient()
            main_page.drag_ingredient_bun_to_basket()

        with allure.step("Получаем новый счётчик и проверяем увеличение"):
            final_count = main_page.get_ingredient_counter()
            assert final_count > original_count
