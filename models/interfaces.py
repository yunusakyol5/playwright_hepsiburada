from abc import ABC, abstractmethod
from playwright.sync_api import Page

class PageInterface(ABC):
    """Interface for all pages"""
    @abstractmethod
    def navigate(self, url: str):
        pass
    
class ProductContainer(ABC):
    """Interface for all pages that contain products"""
    @abstractmethod
    def get_title(self):
        pass
    
    @abstractmethod
    def get_stock_code(self):
        pass 