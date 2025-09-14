from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
    BUN = (By.XPATH, ".//*[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (By.XPATH, ".//*[@class='counter_counter__num__3nue1']")
    MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    OVERLAY_ANIMATION = (By.XPATH, "//img[@alt ='loading animation']")
    MODAL_CONTENT_BOX = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    BASKET_LIST = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

class OrderPageLocators:
    COUNTER_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    ORDER_NUMBERS = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")