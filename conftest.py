import time

import allure
import pytest
from playwright.sync_api import sync_playwright

BROWSERS = [
    "chromium",
    "firefox",
    "webkit"
]


@pytest.fixture(scope="function", params=BROWSERS)
def page(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch(headless=HEADLESS)
        context = browser.new_context()
        # context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        time.sleep(4)
        yield page
        # context.tracing.stop(path=f"trace_{page}.zip")
        context.close()
        browser.close()


@pytest.fixture(autouse=True)
def screenshot(page):
    yield
    allure.attach(page.screenshot(), "screenshot", allure.attachment_type.PNG)
