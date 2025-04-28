class ProductPageLocators:
    """Locators for the product page"""
    TITLE = "h1[data-test-id='title']"
    KEY_FEATURES_TABLE = "[data-test-id='KeyFeaturesTable']"
    ADD_TO_CART_BUTTON = "button[data-test-id='addToCart']"
    PRODUCT_ADDED_CONFIRMATION = "div[class^='checkoutui-ProductOnBasketHeader-']"
    GO_TO_CART_BUTTON_NAME = "Sepete Git"

class CartPageLocators:
    """Locators for the cart page"""
    CART_ITEM_LIST = "#onboarding_item_list"
    CART_ITEM = "li[data-sku]"
    ITEM_TITLE = "div[class^='product_name_'] > a"

class HomePageLocators:
    """Locators for the home page"""
    SEARCH_BAR = "input[data-test-id='search-bar-input']"
    SEARCH_POPUP = "div[aria-label='Popüler aramalar alanı']"
    
class SearchPageLocators:
    """Locators for the search page"""
    PRODUCT_CARDS = "div[aria-label='Ürünler']" 