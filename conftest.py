import os
import time

import allure
import pytest
from playwright.sync_api import sync_playwright

BROWSERS = [
    "chromium",
    "firefox",
    "webkit"
]

HEADLESS = True
if os.path.isfile(os.path.join(os.path.dirname(__file__), 'local_settings.py')):
    import local_settings

    HEADLESS = local_settings.HEADLESS


@pytest.fixture(scope="function", params=BROWSERS)
def page(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch(headless=HEADLESS)
        context = browser.new_context()
        # context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        yield page
        # context.tracing.stop(path=f"trace_{page}.zip")
        context.close()
        browser.close()


@pytest.fixture(autouse=True)
def screenshot(page):
    yield
    allure.attach(page.screenshot(), "screenshot", allure.attachment_type.PNG)


# со Степика посмотреть настройки - https://stepik.org/lesson/826367/step/3?unit=829900
# https://stepik.org/lesson/826369/step/2?unit=829902
# https://stepik.org/lesson/826356/step/7?unit=829889
# https://stepik.org/lesson/826356/step/8?unit=829889
# https://stepik.org/lesson/826356/step/11?unit=829889
# https://stepik.org/lesson/826357/step/1?unit=829890
# https://stepik.org/lesson/825696/step/2?unit=829210