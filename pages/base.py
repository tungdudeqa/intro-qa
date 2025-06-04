import os
import dotenv

dotenv.load_dotenv()

class BasePage:
    BASE_URL = os.getenv("BASE_URL", "")
    BASE_EMAIL = os.getenv("RETAILER_EMAIL", "")
    BASE_PASSWORD = os.getenv("RETAILER_PASSWORD", "")
    BASE_OTP = os.getenv("OTP_CODE", "")

    def __init__(self, page):
        self.page = page
    
    def goto(self, path="/"):
        self.page.goto(self.BASE_URL + path)