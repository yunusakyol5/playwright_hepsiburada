import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = Path(".playwright-screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

DEFAULT_VIEWPORT = {
    "width": 1280,
    "height": 720,
}

@pytest.fixture(scope="function")
def page():
    """Create a new page for each test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Headless mode is False, because Hepsiburada website is blocking headless mode.
        context = browser.new_context(
            viewport=DEFAULT_VIEWPORT,
            screen=DEFAULT_VIEWPORT,
        )
        pg = context.new_page()
        #pg.bring_to_front()  # Bring the page to the front in headed mode
        yield pg
        context.close()
        browser.close()
