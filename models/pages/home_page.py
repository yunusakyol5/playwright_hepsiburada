import re
from urllib.parse import quote_plus
from playwright.sync_api import expect
from models.pages.base_page import BasePage
from models.locators import HomePageLocators


class HomePage(BasePage):
    """Home page of the Hepsiburada website"""
    expected_search_url = "https://www.hepsiburada.com/ara?q="
    
    def __init__(self, page):
        super().__init__(page)
        self.locators = HomePageLocators

    def search(self, keyword):
        """Search for a product via search bar"""
        search_bar = self.wait_for_element(self.locators.SEARCH_BAR, state="editable")
        search_bar.press("Enter")

        expect(self.page.locator(self.locators.SEARCH_POPUP)).to_be_visible(timeout=self.default_timeout)
        search_bar.fill(keyword)

        expect(search_bar).to_have_value(re.compile(keyword), timeout=self.default_timeout)
        search_bar.press("Enter")

    def verify_search(self, keyword):
        """Verify the search result with the expected URL"""
        self.page.wait_for_load_state("load", timeout=self.default_timeout)
        expected_url = self.expected_search_url + quote_plus(keyword)
        expect(self.page).to_have_url(expected_url, timeout=self.default_timeout)
