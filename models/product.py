class Product:
    """Product model"""
    def __init__(self, stock_code, title):
        """Initialize the product
        Args:
            stock_code: str --> Stock code of the product which is unique
            title: str --> Title of the product
        """
        if not stock_code:
            raise ValueError("Stock code cannot be empty")
        if not title:
            raise ValueError("Title cannot be empty")
            
        self.stock_code = stock_code 
        self.title = title

    def serialize(self):
        return {
            "stock_code": self.stock_code,
            "title": self.title
        }
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return (self.stock_code == other.stock_code and
                self.title == other.title)
                
    def __str__(self):
        return f"Product(stock_code='{self.stock_code}', title='{self.title}')"
    
    