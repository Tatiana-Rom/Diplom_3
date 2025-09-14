import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
    def test_total_orders_counter_increases(self, login_user):
        main_page = MainPage(login_user)
        order_page = OrderPage(login_user)

        with allure.step("Открываем раздел Ленты заказов и запоминаем текущее значение счётчика"):
            main_page.wait_for_page_to_load()
            main_page.click_on_feed_button()
            order_page.wait_for_order_page_to_load()
            original_value = order_page.get_total_orders_count()

        with allure.step("Создаём новый заказ"):
            main_page.click_on_constructor_button()
            main_page.wait_for_page_to_load()
            main_page.drag_ingredient_bun_to_basket()
            main_page.place_order()
            order_number = main_page.get_order_number()
            main_page.close_order_success_modal()

        with allure.step("Проверяем, что счётчик увеличился"):
            main_page.click_on_feed_button()
            order_page.wait_for_order_page_to_load()
            updated_value = order_page.get_total_orders_count()
            assert updated_value > original_value

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_orders_counter_increases(self, login_user):
        main_page = MainPage(login_user)
        order_page = OrderPage(login_user)

        with allure.step("Открываем раздел Ленты заказов и запоминаем текущее значение счётчика"):
            main_page.wait_for_page_to_load()
            main_page.click_on_feed_button()
            order_page.wait_for_order_page_to_load()
            original_value = order_page.get_today_orders_count()

        with allure.step("Создаём новый заказ"):
            main_page.click_on_constructor_button()
            main_page.wait_for_page_to_load()
            main_page.drag_ingredient_bun_to_basket()
            main_page.place_order()
            main_page.get_order_number()
            main_page.close_order_success_modal()

        with allure.step("Проверяем, что счётчик увеличился"):
            main_page.click_on_feed_button()
            order_page.wait_for_order_page_to_load()
            updated_value = order_page.get_today_orders_count()
            assert updated_value > original_value

    @allure.title("Номер нового заказа появляется в разделе «В работе»")
    def test_new_order_appears_in_work_list(self, login_user):
        main_page = MainPage(login_user)
        order_page = OrderPage(login_user)

        with allure.step("Создаём новый заказ и сохраняем его номер"):
            main_page.wait_for_page_to_load()
            main_page.drag_ingredient_bun_to_basket()
            main_page.place_order()
            order_number = main_page.get_order_number()
            main_page.close_order_success_modal()

        with allure.step("Проверяем, что заказ отображается в разделе 'В работе'"):
            main_page.click_on_feed_button()
            order_page.wait_for_order_page_to_load()
            in_progress_number = order_page.get_order_number_from_in_progress_section()
            assert order_number == in_progress_number