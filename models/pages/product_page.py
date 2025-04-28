import json
from conftest import SCREENSHOT_DIR
from models.pages.base_page import BasePage
from playwright.sync_api import expect
from models.product import Product
from models.locators import ProductPageLocators
from models.interfaces import ProductContainer
from datetime import datetime

class ProductPage(BasePage, ProductContainer):
    """Product page that contains product details"""
    def __init__(self, page):
        super().__init__(page)
        self.locators = ProductPageLocators
        self.product = Product(
            self.get_stock_code(),
            self.get_title()
        )

    def get_title(self):
        """Get the title of the product"""
        title_locator = self.wait_for_element(self.locators.TITLE)
        return title_locator.inner_text().strip()
    
    def get_stock_code(self):
        """Get the stock code of the product"""
        root = self.wait_for_element(self.locators.KEY_FEATURES_TABLE)
        hbus_raw = root.get_attribute("data-hbus")
        hbus_json = json.loads(hbus_raw)
        return hbus_json["data"]["page_value"]
    
    def add_to_cart(self):
        """Add the product to the car and navigate to the cart page"""
        add_to_cart_button = self.wait_for_element(self.locators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

        try:
            expect(self.page.locator(self.locators.PRODUCT_ADDED_CONFIRMATION).first).to_be_visible(timeout=self.default_timeout)
        except Exception as e:
            timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
            self.page.screenshot(path=SCREENSHOT_DIR / f"assertion_failure_{timestamp}.png", full_page=True)
            raise e
        
        go_to_cart_button = self.page.get_by_role("button", name=self.locators.GO_TO_CART_BUTTON_NAME).first
        expect(go_to_cart_button).to_be_visible(timeout=self.default_timeout)

        with self.page.expect_navigation(timeout=self.default_timeout) as nav:
            go_to_cart_button.click()
        
        return self.page, self.product
    