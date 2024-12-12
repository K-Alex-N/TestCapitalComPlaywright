from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "[data-test='username']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-button']"
        self.title = "[data-test='title']"

    def login(self, username: str, password: str):
        """Выполнение авторизации."""
        self.fill_input(self.username_input, username)
        self.fill_input(self.password_input, password)
        self.click(self.login_button)

    def is_login_successful(self) -> bool:
        """Проверка успешной авторизации."""
        return self.is_visible(self.title)