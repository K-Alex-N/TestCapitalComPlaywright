import allure
import pytest
from playwright.sync_api import sync_playwright

BROWSERS = ["chromium",
            "firefox",
            "webkit"
            ]

@pytest.fixture(scope="function", params=BROWSERS)
def page(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        allure.attach(page.screenshot(), "screenshot", allure.attachment_type.PNG)
        context.close()
        browser.close()
