from playwright.sync_api import Playwright, sync_playwright, expect


def ex_test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # Создаём новый контекст браузера (это изолированная сессия)
    context = browser.new_context()
    # Открываем новую вкладку
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').click()
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').click()
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page.locator('[data-test="title"]')).to_be_visible()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    ex_test(playwright)
