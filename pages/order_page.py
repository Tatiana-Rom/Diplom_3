import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.locators import OrderPageLocators
from data.urls import Urls


class OrderPage(BasePage):

    @allure.step("Открыть страницу Лента заказов")
    def open_order_page(self):
        self.open_page(Urls.ORDER_FEED)

    @allure.step("Проверить, что открыта страница Лента заказов")
    def is_order_page_opened(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(Urls.ORDER_FEED))
        return True

    @allure.step("Ожидание закрытия оверлея")
    def wait_for_overlay_close(self):
        self.wait_for_element_hide(OrderPageLocators.OVERLAY, timeout=15)

    @allure.step("Получить количество заказов Выполнено за всё время")
    def get_total_orders_count(self):
        self.wait_for_overlay_close()
        count = self.get_text_of_element(OrderPageLocators.COUNTER_TOTAL)
        return int(count)

    @allure.step("Получить количество заказов Выполнено за сегодня")
    def get_today_orders_count(self):
        self.wait_for_overlay_close()
        count = self.get_text_of_element(OrderPageLocators.COUNTER_TODAY)
        return int(count)

    @allure.step("Подождать появления заказа в разделе В работе")
    def wait_for_orders_in_progress(self):
        self.wait_for_element_visible(OrderPageLocators.IN_PROGRESS_ORDERS, timeout=15)

    @allure.step("Получить номер заказа из раздела 'В работе'")
    def get_order_number_from_in_progress_section(self):
        self.wait_for_overlay_close()
        WebDriverWait(self.driver, 15).until(
            lambda driver: driver.find_element(*OrderPageLocators.IN_PROGRESS_ORDERS).text.strip().isdigit()
        )

        order_text = self.get_text_of_element(OrderPageLocators.IN_PROGRESS_ORDERS)
        return int(order_text)

    @allure.step("Дождаться загрузки страницы Лента заказов")
    def wait_for_order_page_to_load(self):
        self.wait_for_element_visible(OrderPageLocators.COUNTER_TOTAL)
        self.scroll_to_element(OrderPageLocators.COUNTER_TOTAL)