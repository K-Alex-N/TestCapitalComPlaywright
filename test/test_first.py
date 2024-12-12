# from pages.login_page import LoginPage
from pages.login_page import LoginPage

from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Создаём новый контекст браузера (это изолированная сессия)
        context = browser.new_context()
        # Открываем новую вкладку
        page = context.new_page()
        login_page = LoginPage(page)
        login_page.navigate_to("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_login_successful(), "Не удалось авторизоваться!"

        context.close()
        browser.close()
