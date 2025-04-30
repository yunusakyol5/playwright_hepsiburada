# Hepsiburada Automation with Playwright

A test automation framework built with Python and Playwright to perform end-to-end testing of the Hepsiburada e-commerce website. This project demonstrates how to automate web interactions such as searching for products, adding them to cart, and verifying cart contents.

## Features

- Cross-browser testing using Playwright
- Page Object Model (POM) design pattern implementation
- Parameterized testing for multiple search keywords
- Automatic screenshot capture
- HTML test report generation

## Project Structure

```
playwright_hepsiburada/
├── models/               # Page object models and related classes
│   ├── pages/            # Individual page implementations
│   ├── interfaces.py     # Interface definitions
│   ├── locators.py       # Element locators
│   ├── page_factory.py   # Factory for creating page objects
│   └── product.py        # Product representation
├── tests/                # Test scripts
│   └── test_hepsiburada.py # Main test script
├── .playwright-screenshots/ # Screenshot storage
├── conftest.py           # Pytest configurations and fixtures
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yunusakyol5/playwright_hepsiburada.git
   cd playwright_hepsiburada
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Install Playwright browsers:
   ```bash
   python -m playwright install
   ```

## Usage

### Running Tests

To run the tests:
```bash
pytest tests/test_hepsiburada.py
```

To run with screenshot option:
```bash
pytest tests/test_hepsiburada.py --screenshot=only-on-failure
```

To run with HTML report generation:
```bash
pytest tests/test_hepsiburada.py --html=report.html
```

To run a desired number of times:
```bash
pytest tests/test_hepsiburada.py --count "NUM_of_DESIRED_TESTS" 
```

To run with parallel workers:
```bash
pytest tests/test_hepsiburada.py -n "NUM_of_WORKERS" 
```

### Viewing Reports

After running tests with the HTML reporter, open `report.html` in your browser to view detailed test results.

## Notes

- The tests run in headed mode (with browser UI visible) because Hepsiburada blocks headless browser access
- Screenshots are saved in the `.playwright-screenshots` directory when tests fail
- The framework tests multiple product categories: laptop, kulaklık (headphones), buzdolabı (refrigerator), and telefon (phone)
