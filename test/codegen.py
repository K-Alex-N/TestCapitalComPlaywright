from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Инициализируем LoginPage
        login_page = LoginPage(page)

        # Переходим на страницу авторизации
        login_page.navigate_to("<https://www.saucedemo.com/>")

        # Выполняем вход
        login_page.login("standard_user", "secret_sauce")

        # Проверяем успешность входа
        assert login_page.is_login_successful(), "Не удалось авторизоваться!"

        # Закрываем контекст и браузер
        context.close()
        browser.close()