from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    def __init__(self, page):
        with allure.step("Initialize LoginPage"):
            super().__init__(page)
            self.username_input = "[data-test='username']"
            self.password_input = "[data-test='password']"
            self.login_button = "[data-test='login-button']"
            self.title = "[data-test='title']"

    def login(self, username: str, password: str):
        with allure.step("Perform login"):
            self.fill_input(self.username_input, username)
            self.fill_input(self.password_input, password)
            self.click(self.login_button)

    def is_login_successful(self) -> bool:
        with allure.step("Verify successful login"):
            return self.is_visible(self.title)
