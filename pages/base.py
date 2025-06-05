import os
import dotenv
import logging

dotenv.load_dotenv()
logger = logging.getLogger("logger")

class BasePage:
    BASE_URL = os.getenv("BASE_URL", "")
    BASE_EMAIL = os.getenv("RETAILER_EMAIL", "")
    BASE_PASSWORD = os.getenv("RETAILER_PASSWORD", "")
    BASE_OTP = os.getenv("OTP_CODE", "")
    logger = logger

    def __init__(self, page,):
        self.page = page
        self.locators = {}
        self.elem = lambda x, **kwargs: (
            self.page.locator(self.locators[x].format(**kwargs))
            if kwargs else self.page.locator(self.locators[x])
        )
    
    def goto(self, path="/"):
        self.page.goto(self.BASE_URL + path)