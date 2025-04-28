from playwright.sync_api import Page, expect
from models.interfaces import PageInterface

class BasePage(PageInterface):
    """Base page class that contains common methods for all pages"""
    def __init__(self, page: Page):
        self.page = page
        self.default_timeout = 30_000

    def navigate(self, url: str):
        """Navigate to the given URL"""
        self.page.goto(url, wait_until="load")
        self.block_third_party()

    def block_third_party(self):
        """Block third party ads"""
        ad_hosts = ("doubleclick.net", "googlesyndication.com")
        self.page.context.route("**/*", lambda route, req:
            route.abort() if any(h in req.url for h in ad_hosts) else route.continue_()
        )
        self.page.wait_for_load_state("load", timeout=self.default_timeout)
        
    def wait_for_element(self, selector, state="visible"):
        """Centralized wait method for elements"""
        locator = self.page.locator(selector).first
        if state == "visible":
            expect(locator).to_be_visible(timeout=self.default_timeout)
        elif state == "enabled":
            expect(locator).to_be_enabled(timeout=self.default_timeout)
        elif state == "editable":
            expect(locator).to_be_editable(timeout=self.default_timeout)
        return locator
