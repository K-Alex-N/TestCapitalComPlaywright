from playwright.sync_api import Playwright, sync_playwright, expect


# Основная функция для запуска теста
def ex_test(playwright: Playwright) -> None:
    # Запускаем Chromium браузер в режиме с GUI (headless=False)
    browser = playwright.chromium.launch(headless=False)

    # Создаём новый контекст браузера (это изолированная сессия)
    context = browser.new_context()

    # Открываем новую вкладку
    page = context.new_page()

    # Переходим на сайт
    page.goto("<https://www.saucedemo.com/>")

    # Заполняем поле "username"
    page.locator("[data-test=\\"username\\"]").click()
    page.locator("[data-test=\\"username\\"]").fill("standard_user")

    # Заполняем поле "password"
    page.locator("[data-test=\\"password\\"]").click()
    page.locator("[data-test=\\"password\\"]").fill("secret_sauce")

    # Нажимаем на кнопку "Login"
    page.locator("[data-test=\\"login - button\\"]").click()

    # Проверяем, что страница успешно загружена (проверка на видимость элемента)
    expect(page.locator("[data-test=\\"title\\"]")).to_be_visible()

    # Закрываем контекст и браузер после завершения работы
    context.close()
    browser.close()


# Используем Playwright в синхронном режиме для запуска основного кода
with sync_playwright() as playwright:
    ex_test(playwright)