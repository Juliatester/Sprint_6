import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Users
from locators.main_page_locators import SiteHeaderLocators


test_data = [
    (Users.user_1, MainPage.click_order_button_header, "Заказ: пользователь 1, кнопка в шапке"),
    (Users.user_2, MainPage.click_order_button_footer, "Заказ: пользователь 2, кнопка внизу"),
]

@allure.suite("Оформление заказа самоката")
class TestOrder:
    
    @pytest.mark.parametrize('user, click_entry, desc', test_data)
    @allure.title("{desc}")
    @allure.description("Заказ самоката для двух пользователей.")
    def test_order_positive_flow(self, driver, user, click_entry, desc):
        main = MainPage(driver)
        with allure.step("Переходим к форме заказа"):
            click_entry(main)
        order_page = OrderPage(driver)
        with allure.step("Заполняем личных данных"):
            order_page.user_info(user)
        with allure.step("Заполняем данных по аренде"):
            order_page.rent_info(user)
        with allure.step("Подтверждаем заказа"):
            order_page.confirm_order()
        with allure.step("Проверяем появилось ли модальное окно успешного заказа"):
            assert order_page.is_order_success(), "Окно успешного заказа не появилось"