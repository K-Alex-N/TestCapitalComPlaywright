import allure
from playwright.sync_api import Page, expect


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
            return self.page.locator(selector).is_visible(timeout=1000)

    def hover_over(self, selector: str):
        with allure.step(f"Hover over element -> {selector}"):
            self.page.locator(selector).hover()

    def get_text(self, selector: str):
        return self.page.locator(selector).text_content()

    def to_close_cookies_pop_up_window(self):
        with allure.step("Accept all cookies"):
            self.click('button#onetrust-accept-btn-handler')

    def reload_page(self):
        self.page.reload()

    def search_and_open_an_article_in_market_analysis_page(self, part_of_article_title):

        ARTICLE_LOCATOR = f"//div[@id='alc']//b[contains(text(), '{part_of_article_title}')]"
        # LOCATOR_LINK_NEXT_PAGE = '//a[@aria-label="Go to the next page"]'
        LOCATOR_LINK_NEXT_PAGE = '[aria-label="Go to the next page"]'
        # div.ot-search-cntr


        def is_article_present() -> bool:
            return self.is_visible(ARTICLE_LOCATOR)

        def open_the_article():
            self.click(ARTICLE_LOCATOR)

        def go_to_next_page():
            self.click(LOCATOR_LINK_NEXT_PAGE)

        def is_there_next_page() -> bool:
            return self.is_visible(LOCATOR_LINK_NEXT_PAGE)

        self.page.wait_for_selector(LOCATOR_LINK_NEXT_PAGE)
        while True:
            print("1 ", is_article_present())
            # expect(self.page.locator(ARTICLE_LOCATOR)).to_be_visible(visible=True)
            print("2 ", is_there_next_page())
            if is_article_present():
                open_the_article()
                return

            if is_there_next_page():
                go_to_next_page()
                continue
            break

        raise Exception("All pages were checked. Artile was not found.")