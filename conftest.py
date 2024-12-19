import allure
import pytest
from playwright.sync_api import sync_playwright

BROWSERS = ["chromium",
            # "firefox",
            # "webkit"
            ]


@pytest.fixture(scope="function", params=BROWSERS)
def page(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(autouse=True)
def screenshot(page):
    yield
    allure.attach(page.screenshot(), "screenshot", allure.attachment_type.PNG)
