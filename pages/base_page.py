import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        with allure.step(f"Navigate to URL -> {url}"):
            self.page.goto(url)

    def click(self, selector: str):
        with allure.step(f"Click element -> {selector}"):
            self.page.locator(selector).click()

    def fill_input(self, selector: str, value: str):
        with allure.step(f"Fill input -> {selector} with value: {value}"):
            self.page.locator(selector).fill(value)

    def is_visible(self, selector: str) -> bool:
        with allure.step(f"Check if element is visible -> {selector}"):
            return self.page.locator(selector).is_visible()

    def hover_over(self, selector: str):
        with allure.step(f"Hover over element -> {selector}"):
            self.page.locator(selector).hover()

    def to_close_cookies_pop_up_window(self):
        with allure.step("To close pop up window about cookies"):
            self.click('button#onetrust-accept-btn-handler')

    def search_and_open_an_article_in_market_analysis_page(self, part_of_article_title):

        ARTICLE_LOCATOR = (By.XPATH, f"//div[@id='alc']//b[contains(text(), '{part_of_article_title}')]")
        LOCATOR_LINK_NEXT_PAGE = (By.XPATH, '//a[@aria-label="Go to the next page"]')
        LOCATOR_LAST_PAGE = (By.XPATH, '//a[@aria-label="Go to the next page"]/preceding::a[1]')
        CLOSE_BLUE_BLOCK = (By.CSS_SELECTOR, "div.main_banner__niieI button")


        def get_last_page() -> int:
            try:
                last_page_obj = driver.find_element(*LOCATOR_LAST_PAGE)
                last_page_number = int(last_page_obj.text)
                return last_page_number
            except:
                raise Exception("Last page number was not found")

        def is_article_present():
            try:
                driver.find_element(*ARTICLE_LOCATOR)
                return True
            except:
                return False

        def to_close_blue_block():
            try:
                driver.find_element(*CLOSE_BLUE_BLOCK).click()
            except:
                return

        def open_the_article():
            to_close_blue_block()
            driver.find_element(*ARTICLE_LOCATOR).click()

        def go_to_next_page():
            driver.find_element(*LOCATOR_LINK_NEXT_PAGE).click()

        last_page = get_last_page()

        for _ in range(1, last_page + 1):
            if is_article_present():
                open_the_article()
                return
            else:
                go_to_next_page()

        raise Exception(f"{last_page} pages were checked. Artile was not found.")