from pages.base_page import BasePage
import allure


class Locators:
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    TITLE = "[data-test='title']"


class LoginPage(BasePage):
    def __init__(self, page):
        with allure.step("Initialize LoginPage"):
            super().__init__(page)

    def login(self, username: str, password: str):
        with allure.step("Perform login"):
            self.fill_input(Locators.USERNAME_INPUT, username)
            self.fill_input(Locators.PASSWORD_INPUT, password)
            self.click(Locators.LOGIN_BUTTON)

    def is_login_successful(self) -> bool:
        with allure.step("Verify successful login"):
            return self.is_visible(Locators.TITLE)
