import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        with allure.step(f"Navigate to URL: {url}"):
            self.page.goto(url)

    def click(self, selector: str):
        with allure.step(f"Click element: {selector}"):
            self.page.locator(selector).click()

    def fill_input(self, selector: str, value: str):
        with allure.step(f"Fill input: {selector} with value: {value}"):
            self.page.locator(selector).fill(value)

    def is_visible(self, selector: str) -> bool:
        with allure.step(f"Check if element is visible: {selector}"):
            return self.page.locator(selector).is_visible()
