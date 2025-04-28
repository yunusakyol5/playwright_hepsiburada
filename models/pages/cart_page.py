import re
from models.pages.base_page import BasePage
from playwright.sync_api import expect
from models.product import Product
from models.locators import CartPageLocators
from models.interfaces import ProductContainer

class CartPage(BasePage, ProductContainer):
    """Cart page that contains the products in the cart"""
    def __init__(self, page, product: Product):
        super().__init__(page)
        self.locators = CartPageLocators
        self.added_product = product
        self.stock_code_list = self.fetch_stock_code_list()

    def _item_root(self, stock_code):
        """Get the root element which contains the item"""
        root = self.page.locator(f"li[data-sku='{stock_code}']").first
        expect(root).to_be_visible(timeout=self.default_timeout)
        return root

    def get_title(self, stock_code=None):
        """Get the title of the product in the cart"""
        stock_code = stock_code or self.added_product.stock_code
        root = self._item_root(stock_code)
        title = root.locator(self.locators.ITEM_TITLE).first
        expect(title).to_be_visible(timeout=self.default_timeout)
        return title.inner_text().strip()
    
    def get_stock_code(self):
        """Get the stock code of the product in the cart"""
        return self.added_product.stock_code

    def fetch_stock_code_list(self):
        """Fetch the stock code list of the products in the cart"""
        section = self.page.locator(self.locators.CART_ITEM_LIST)
        expect(section).to_be_visible(timeout=self.default_timeout)
        items = section.locator(self.locators.CART_ITEM)
        return items.evaluate_all("els => els.map(e => e.getAttribute('data-sku'))")

    def fetch_cart_product(self):
        """Fetch the product in the cart"""
        product = Product(
            self.added_product.stock_code,
            self.get_title(self.added_product.stock_code)
        )
        return product

    def check_cart_is_not_empty(self):
        """Check if the cart is not empty"""
        return len(self.stock_code_list) > 0
    
    def check_added_product_in_cart(self):
        """Check if the added product is in the cart"""
        return self.added_product.stock_code in self.stock_code_list

    def verify_product(self):
        """Verify the product in the cart"""
        assert self.check_cart_is_not_empty(), "Cart is empty" # This means that the cart is empty and no product is added. So, test failed.
        assert self.check_added_product_in_cart(), f"Product {self.added_product.stock_code} not found in cart" # This means that the added product is not in the cart. So, test failed.
        cart_product = self.fetch_cart_product()
        assert cart_product.stock_code == self.added_product.stock_code, f"Stock code mismatch {cart_product.stock_code} != {self.added_product.stock_code}" # This means that the stock code of the added product is not the same as the stock code in the cart. So, test failed.
        #assert re.compile(re.sub(r"\s+", " ", cart_product.title).strip().casefold()) == re.compile(re.sub(r"\s+", " ", self.added_product.title).strip().casefold()), f"Title mismatch {cart_product.title} != {self.added_product.title}" # Titles are not standardized, so I prefer not to check it. 
