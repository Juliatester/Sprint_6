import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import SiteHeaderLocators

class MainPage(BasePage):

    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_order_button_header(self):
        self.scroll_and_safe_click(SiteHeaderLocators.header_order_button)
        
    @allure.step('Клик по кнопке "Заказать" в футере')
    def click_order_button_footer(self):
        self.scroll_and_safe_click(SiteHeaderLocators.body_order_button)

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(SiteHeaderLocators.yandex_logo)

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(SiteHeaderLocators.scooter_logo)

    @allure.step('Выбрать вопрос FAQ №{index}')
    def click_faq_question(self, index):
        loc = SiteHeaderLocators.faq_headings[index]
        self.scroll_and_safe_click(loc)
        
    @allure.step('Получить текст ответа на вопрос FAQ №{index}')
    def get_faq_answer_text(self, index):
        loc = SiteHeaderLocators.faq_contents[index]
        return self.wait_and_get_text(loc)