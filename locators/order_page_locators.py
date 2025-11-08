from selenium.webdriver.common.by import By

class OrderPageLocators:
    """ Форма Про аренду """
    date_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    period_dropdown_toggle = (By.CSS_SELECTOR, "span.Dropdown-arrow")
    period_one_day = (By.XPATH, ".//div[text()='сутки']")
    period_three_days = (By.XPATH, ".//div[text()='трое суток']")

    # Выбор цвета самоката
    black_scooter = (By.ID, "black")
    grey_scooter = (By.ID, "grey")

    # Комментарий и кнопка "Заказать"
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button_finish = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    """ Окно Хотите оформить заказ? """
    # Кнопка Да в окне подтверждения
    order_yes_btn = (By.XPATH, "//button[text() = 'Да']")

    """ Окно подтверждения успешного оформления заказа """
    # Кнопка Посмотреть статус
    status_order_button = (By.XPATH, "//button[text()='Посмотреть статус']")

    """" Форма Для кого самокат """
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")