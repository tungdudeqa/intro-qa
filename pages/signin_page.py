import time
from pages.base import BasePage
from playwright.sync_api import expect
import pytest

class SigninPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = {
            "title": '//div[contains(@class, "title")]',
            "subtitle": '//div[contains(@class, "description")]',
            "email_input_label": '//*[@data-testid="email-input-label"]',
            "email_input_error_label": '//*[@data-testid="email-input-error-label"]',
            "email_input": '//*[@data-testid="email-input"]',
            "password_input_label": '//*[@data-testid="password-input-label"]',
            "password_input_error_label": '//*[@data-testid="password-input-error-label"]',
            "password_input": '//*[@data-testid="password-input"]',
            'show_password_checkbox': '//*[@data-testid="password-input-checkbox"]',
            'signin_button': '//*[@data-testid="login-btn"]',
            'forgot_password_button': '//*[@data-testid="request-forgot-btn"]',
            'contact_us_link': '//body/div/div/div[2]/div/div/div[2]',
            'platform_name': '//body/div/div/div[1]/div'
        }
        self.elem = lambda x: self.page.locator(self.locators[x])

    def check_elements_presence(self):
        self.page.goto(self.BASE_URL + "/")

        try:
            expect(self.elem("title")).to_have_text("Welcome")
            expect(self.elem("subtitle")).to_have_text(
                "Log in to continue using our platform."
            )
            expect(self.elem("email_input_label")).to_have_text("Email")
            expect(self.elem("email_input")).to_have_attribute(
                "placeholder", "Enter your email"
            )
            expect(self.elem("password_input_label")).to_have_text("Password")
            expect(self.elem("password_input")).to_have_attribute(
                "placeholder", "Enter your password"
            )

            self.elem("show_password_checkbox").is_visible()
            expect(self.elem("show_password_checkbox")).to_have_text("Show password")

            expect(self.elem("signin_button")).to_be_visible()
            expect(self.elem("signin_button")).to_have_text("Sign in")
            expect(self.elem("forgot_password_button")).to_be_visible()
            expect(self.elem("forgot_password_button")).to_have_text("Forgot password?")

            # Please contacttest@test.comif you need any more help -- in the web right now
            # expect(self.elem("contact_us_link")).to_have_text("Please contact support@sertiscorp.com if you need any more help")

            expect(self.elem("platform_name").locator('div').nth(0)).to_have_text("Data Commercialization Platform")
            expect(self.elem("platform_name").locator('div').nth(1)).to_have_text("Powered by Sertis")
        except Exception as e:
            pytest.fail(f"Element presence check failed: {e}")

    def signin(self):
        email = self.BASE_EMAIL
        password = self.BASE_PASSWORD

        self.page.goto(self.BASE_URL + "/")
        self.elem("email_input").fill(email)
        self.elem("password_input").fill(password)

        show_password_checkbox = self.elem("show_password_checkbox")
        show_password_checkbox.click()
        expect(self.elem("password_input")).to_have_attribute("type", "text")
        show_password_checkbox.click()
        expect(self.elem("password_input")).to_have_attribute("type", "password")

        self.elem("signin_button").click()
        expect(self.page).to_have_url(self.BASE_URL + "/en/platform/reports", timeout=10000)
    
    def signin_invalid(self, email, password):
        assert not(email == "correct" and password == "correct"), "Email and password should not be both correct for this test."

        if email == "correct":
            email = self.BASE_EMAIL
        if password == "correct":
            password = self.BASE_PASSWORD
        
        self.page.goto(self.BASE_URL + "/")
        self.elem("email_input").fill(email)
        self.elem("password_input").fill(password)
        self.elem("signin_button").click()

        expect(self.elem("email_input_error_label")).to_have_text("Email or password is incorrect. Please try again.")
        expect(self.elem("password_input_error_label")).to_have_text("Email or password is incorrect. Please try again.")
