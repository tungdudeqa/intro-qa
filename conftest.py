import os
import pytest
from playwright.sync_api import sync_playwright

def pytest_logger_config(logger_config):
    logger_config.add_loggers(['logger'], stdout_level='info')
    logger_config.set_log_option_default('logger')

def pytest_logger_logdirlink(config):
    return os.path.join(os.path.dirname(__file__), 'tlogs')

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()