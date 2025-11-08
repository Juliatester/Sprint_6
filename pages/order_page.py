import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import Users
from selenium.webdriver.common.by import By
from locators.main_page_locators import SiteHeaderLocators

class OrderPage(BasePage):
    @allure.step('Заполняем контактные данные пользователя')
    def user_info(self, user):
        self.enter_text(OrderPageLocators.name_field, user['name'])
        self.enter_text(OrderPageLocators.surname_field, user['surname'])
        self.enter_text(OrderPageLocators.address_field, user['address'])
        self.choose_metro(user['subway'])
        self.enter_text(OrderPageLocators.phone_field, user['phone'])
        self.click(OrderPageLocators.next_button)

    @allure.step('Выбираем ближайшую станцию метро: {subway}')
    def choose_metro(self, subway):
        self.find(OrderPageLocators.metro_field).send_keys(subway)
        self.wait_and_click((By.XPATH, f".//div[text()='{subway}']"))

    @allure.step('Устанавливаем условия аренды самоката')
    def rent_info(self, user):
        self.enter_text(OrderPageLocators.date_field, user['date'])
        self.click(OrderPageLocators.period_dropdown_toggle)
        period_map = {"сутки": OrderPageLocators.period_one_day, "трое суток": OrderPageLocators.period_three_days}
        color_map = {"черный жемчуг": OrderPageLocators.black_scooter, "серая безысходность": OrderPageLocators.grey_scooter}
        self.click(period_map[user['period_type']])
        self.click(color_map[user['color']])
        self.enter_text(OrderPageLocators.comment_field, user['comment'])
        self.click(OrderPageLocators.order_button_finish)

    @allure.step('Подтверждаем оформление заказа')
    def confirm_order(self):
        self.click(OrderPageLocators.order_yes_btn)

    @allure.step('Проверяем успешность заказа')
    def is_order_success(self):
        return self.element_is_displayed(OrderPageLocators.status_order_button)