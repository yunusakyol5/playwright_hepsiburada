import pytest
from models.page_factory import PageFactory

@pytest.mark.parametrize("keyword", ["laptop", "kulaklık", "buzdolabı", "telefon"])
def test_add_product_to_cart(page, keyword):
    """Test to search a product, add it to the cart and verify the product in the cart"""
    # Use page factory to create pages
    factory = PageFactory()
    
    # Create home page and start the flow
    home_page = factory.create_home_page(page)
    home_page.navigate("https://www.hepsiburada.com")
    home_page.search(keyword)
    home_page.verify_search(keyword)
    
    # Create search page
    search_page = factory.create_search_page(home_page.page)
    selected_product_page = search_page.select_product()
    
    # Create product page
    product_page = factory.create_product_page(selected_product_page)
    cart_page, product = product_page.add_to_cart()
    
    # Create cart page
    cart = factory.create_cart_page(cart_page, product)
    cart.verify_product()
