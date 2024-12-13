import allure
from allure import step
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # @step(f"Navigate to URL: {url}")
    def navigate_to(self, url: str):
        """Переход на указанный URL."""
        with allure.step(f"Navigate to URL: {url}"):
            self.page.goto(url)

    def click(self, selector: str):
        """Клик по элементу."""
        self.page.locator(selector).click()

    def fill_input(self, selector: str, value: str):
        """Заполнение поля ввода."""
        self.page.locator(selector).fill(value)

    def is_visible(self, selector: str) -> bool:
        """Проверка видимости элемента."""
        return self.page.locator(selector).is_visible()