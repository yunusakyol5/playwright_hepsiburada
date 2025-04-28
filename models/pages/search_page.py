from random import randint
from models.pages.base_page import BasePage
from playwright.sync_api import expect
from models.locators import SearchPageLocators

class SearchPage(BasePage):
    """Search page that contains listed products"""
    def __init__(self, page):
        super().__init__(page)
        self.locators = SearchPageLocators

    def select_product(self):
        """Select a random product from the list and click on it"""
        product_cards = self.page.locator(self.locators.PRODUCT_CARDS)
        selected_product = product_cards.locator("li").nth(randint(0,15))

        expect(selected_product).to_be_enabled(timeout=self.default_timeout)

        with self.page.expect_popup(timeout=self.default_timeout) as popup_info:
            selected_product.click()

        new_page = popup_info.value
        new_page.wait_for_load_state("domcontentloaded", timeout=self.default_timeout)
        return new_page
    