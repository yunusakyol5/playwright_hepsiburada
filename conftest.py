import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

SCREENSHOT_DIR = Path(".playwright-screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

VIDEO_DIR = Path(".playwright-videos")
VIDEO_DIR.mkdir(exist_ok=True)

DEFAULT_VIEWPORT = {
    "width": 1280,
    "height": 720,
}

@pytest.fixture(scope="function")
def page(request):
    """Create a new page for each test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Headless mode is False, because Hepsiburada website is blocking headless mode.
        
        # Configure context with standard options
        context_options = {
            "viewport": DEFAULT_VIEWPORT,
            "screen": DEFAULT_VIEWPORT,
        }
        
        context = browser.new_context(**context_options)
        pg = context.new_page()
        
        yield pg
        
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test result information available to fixtures."""
    outcome = yield
    rep = outcome.get_result()
    
    # Set a report attribute for each phase of a call
    setattr(item, f"rep_{rep.when}", rep)


