import pytest
from playwright.sync_api import sync_playwright

BROWSERS = ["chromium",
            "firefox",
            # "webkit"
            ]

@pytest.fixture(scope="function", params=BROWSERS)
def browser_context(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, request.param)
        browser = browser_type.launch()
        context = browser.new_context()
        yield context
        context.close()
        browser.close()
