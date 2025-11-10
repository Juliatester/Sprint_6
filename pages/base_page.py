import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент: {locator}')
    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажать на элемент: {locator}')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Ввести текст "{text}" в поле: {locator}')
    def enter_text(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)

    @allure.step('Получить текст из элемента: {locator}')
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step('Прокрутить страницу до элемента: {locator}')
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидать смену адреса на {expected_url}')
    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

    @allure.step('Проверить наличие элемента: {locator}')
    def element_is_displayed(self, locator):
        return self.find(locator).is_displayed()

    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидать открытие новой вкладки')
    def wait_for_new_tab(self, tabs):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > len(tabs))

    @allure.step('Перехватить управление последней открытой вкладкой')
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Убедиться, что URL загруженной страницы валиден')
    def wait_for_url_is_not_blank(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")

    @allure.step('Ожидать доступности элемента и кликнуть по нему: {locator}')
    def wait_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ожидать отображения элемента и извлечь текст: {locator}')
    def wait_and_get_text(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

    @allure.step('Двойной клик по элементу с предварительным скроллом: {locator}')
    def scroll_and_safe_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("window.scrollBy(0, -100);")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Загрузить страницу по указанному адресу: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Вернуть список открытых окон браузера')
    def get_window_handles(self):
        return self.driver.window_handles