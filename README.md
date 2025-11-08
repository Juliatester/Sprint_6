# Sprint_6
Тестирование веб-приложения "Самокат"
Описание проекта:
Этот проект содержит автоматизированные тесты для веб-приложения "Самокат" с использованием фреймворка PyTest и библиотеки Selenium. Тесты проверяют основные функции приложения, такие как оформление заказа, работа с FAQ и навигация по сайту.

Структура проекта
Проект имеет следующую структуру:


Sprint_6/
├── allure_results
├── locators/
│   ├── main_page_locators.py
│   └── order_page_locators.py
├── pages/
│   ├── base_page.py
│   └── main_page.py
│   └── order_page.py
├── tests/
│   ├── test_logo.py
│   ├── test_main_page.py
│   └── test_order.py
├── conftest.py
├── data.py
└── README.md
└── requirements.txt


Требования:
Для запуска тестов требуются следующие зависимости:

Python 3.x
PyTest
Selenium
Allure


Зависимости:
pip install -r requirements.txt

Запусти тесты:
pytest --alluredir=allure-results

Сгенерировать отчёт Allure:
allure serve allure-results

Проект содержит следующие тесты:

test_logo.py: Тесты для проверки навигации по логотипам.
test_main_page.py: Тесты для проверки работы с FAQ.
test_order.py: Тесты для проверки оформления заказа.

Отчёты
Для генерации отчётов используется Allure. После запуска тестов отчёт можно открыть с помощью команды:
allure serve allure-results
