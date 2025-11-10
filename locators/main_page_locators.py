from selenium.webdriver.common.by import By

class SiteHeaderLocators:
    # Логотип Яндекса в верхней панели сайта
    yandex_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")
    # Логотип самоката в верхней панели сайта
    scooter_logo = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    # Кнопка заказа в верхней панели сайта
    header_order_button = (By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")
    # Кнопка заказа в основной области главной страницы
    body_order_button = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']")
    # Логотип Дзена
    logo_dzen = (By.XPATH, "//*[contains(@class, 'header__logoLink')]")

    faq_headings = [(By.ID, f"accordion__heading-{i}") for i in range(8)]
    faq_contents = [(By.ID, f"accordion__panel-{i}") for i in range(8)]
    # Базовые URL страницы
    main_url = "https://qa-scooter.praktikum-services.ru/"
    order_url = "https://qa-scooter.praktikum-services.ru/order"