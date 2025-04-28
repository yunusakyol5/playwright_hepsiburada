from playwright.sync_api import Page
from models.pages.home_page import HomePage
from models.pages.search_page import SearchPage
from models.pages.product_page import ProductPage
from models.pages.cart_page import CartPage
from models.product import Product

class PageFactory:
    """Factory for creating page objects with appropriate dependencies"""
    
    @staticmethod
    def create_home_page(page: Page) -> HomePage:
        return HomePage(page)
    
    @staticmethod
    def create_search_page(page: Page) -> SearchPage:
        return SearchPage(page)
    
    @staticmethod
    def create_product_page(page: Page) -> ProductPage:
        return ProductPage(page)
    
    @staticmethod
    def create_cart_page(page: Page, product: Product) -> CartPage:
        return CartPage(page, product) 