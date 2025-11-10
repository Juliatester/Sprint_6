import allure
from pages.main_page import MainPage
from locators.main_page_locators import SiteHeaderLocators

class TestLogo:

    @allure.title("Переход на главную страницу после клика на логотип Самоката")
    @allure.description("Клик по логотипу Самоката должен возвращать пользователя на главную страницу.")
    def test_click_scooter_logo_redirects_to_home(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем страницу заказа"):
            page.open(SiteHeaderLocators.order_url)
        with allure.step("Кликаем на логотип Самоката"):
            page.click_scooter_logo()
        with allure.step("Проверяем перенаправление на главную страницу"):
            page.wait_for_url(SiteHeaderLocators.main_url)
            current_url = page.get_current_url()
            assert current_url.startswith(SiteHeaderLocators.main_url), f"Ошибка перехода на главную страницу! Ожидаемый URL: {SiteHeaderLocators.main_url}, Текущий URL: {current_url}"

    @allure.title("Проверка перехода на Дзен после клика на логотип Яндекса")
    @allure.description("Клик по логотипу Яндекса должен открыть Дзен в новой вкладке.")
    def test_click_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем страницу заказа"):
            page.open(SiteHeaderLocators.order_url)
        with allure.step("Кликаем на логотип Яндекса"):
            tabs = page.get_window_handles()
            page.click_yandex_logo()
        with allure.step("Ожидаем открытие новой вкладки и переключаемся на неё"):
            page.wait_for_new_tab(tabs)
            page.switch_to_last_tab()
        with allure.step("Проверяем, что открыта страница Дзена"):
            page.wait_for_url_is_not_blank()
            current_url = page.get_current_url()
            assert "dzen.ru" in current_url, f"Дзен не открылся: {current_url}"