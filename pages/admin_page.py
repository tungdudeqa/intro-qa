from pages.signin_page import SigninPage
from playwright.sync_api import expect


class AdminPage(SigninPage):
    def __init__(self, page):
        super().__init__(page)
        self.locators.update(
            {
                "supplier_admin": '//a[@data-testid="supplier-left-bar-test-id-button-1"]',
                "edit_button": '//button[@data-testid="edit-button-test-id"]',
                "first_name_field": '//input[@data-testid="firstName-text-input-id"]',
                "last_name_field": '//input[@data-testid="lastName-text-input-id"]',
                "email_field": '//input[@data-testid="email-text-input-id"]',
                "phone_field": '//input[@data-testid="phone-number-input-test-id-text-input"]',
                "test_row": '//*[@data-testid="undefined-body-row-0"]',
            }
        )
        self.errors = {
            "first_name": {
                "path": '//label[@data-testid="firstName-text-input-id-error-label"]',
                "message": {
                    "empty": "Please enter the admin’s first name before continuing.",
                    "invalid": "This field can only contain alphabetic characters (A-Z, a-z)."
                }
            },
            "last_name": {
                "path": '//label[@data-testid="lastName-text-input-id-error-label"]',
                "message": {
                    "empty": "Please enter the admin’s last name before continuing.",
                    "invalid": "This field can only contain alphabetic characters (A-Z, a-z)."   
                }
            },
            "email": {
                "path": '//label[@data-testid="email-text-input-id-error-label"]',
                "message": {
                    "empty": "Please enter the admin’s email before continuing.",
                    "invalid": "This field must have a valid email format (example@email.com)."
                }
            },
            "phone": {
                "path": '//p[@data-testid="phone-number-input-test-id-error-label"]',
                "message": {
                    "empty": "Please enter the admin’s phone number before continuing.",
                    "invalid": "The country code or phone number is invalid. Please try again.", 
                }
            },
        }

    def _goto(self, edit=False):
        self.signin()
        self.goto("/en/platform/suppliers")
        self.elem("test_row").click()
        self.page.wait_for_load_state("domcontentloaded")
        self.elem("supplier_admin").click()
        self.page.wait_for_load_state("domcontentloaded")
        if edit:
            self.elem("edit_button").click()
            self.page.wait_for_load_state("domcontentloaded")

    def check_error_message(self, field, data):
        self._goto(edit=True)
        self.elem(field + "_field").fill(data)

        if data != "":
            expect(self.page.locator(self.errors[field]['path'])).to_have_text(
                self.errors[field]["message"]["invalid"]
            )
        else:
            expect(self.page.locator(self.errors[field]['path'])).to_have_text(
                self.errors[field]["message"]["empty"]
            )
