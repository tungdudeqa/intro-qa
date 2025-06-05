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
            "logo": '//img[@alt="logo"]',
            "email_input_label": '//*[@data-testid="email-input-label"]',
            "email_input_error_label": '//*[@data-testid="email-input-error-label"]',
            "email_input": '//*[@data-testid="email-input"]',
            "password_input_label": '//*[@data-testid="password-input-label"]',
            "password_input_error_label": '//*[@data-testid="password-input-error-label"]',
            "password_input": '//*[@data-testid="password-input"]',
            "show_password_checkbox": '//*[@data-testid="password-input-checkbox"]',
            "signin_button": '//*[@data-testid="login-btn"]',
            "forgot_password_button": '//*[@data-testid="request-forgot-btn"]',
            "contact_us_link": "//body/div/div/div[2]/div/div/div[2]",
            "contact_email_unsupported": "//body/div/div/div/a",
            "logo_unsupported": '//img[@alt="nav retailer logo"]',
            "platform_name": "//body/div/div/div[1]/div",
            "loading": 'text=Please wait.',
            "spinner": '//*[contains(@class, "animate-spin-fast")]',
        }
        self.elem = lambda x: self.page.locator(self.locators[x])

    def check_elements_presence(self, url="/"):
        self.page.goto(self.BASE_URL + url)

        try:
            expect(self.elem("title")).to_have_text("Welcome")
            expect(self.elem("subtitle")).to_have_text(
                "Log in to continue using our platform."
            )
            expect(self.elem("logo")).to_be_visible()
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

            expect(self.elem("platform_name").locator("div").nth(0)).to_have_text(
                "Data Commercialization Platform"
            )
            expect(self.elem("platform_name").locator("div").nth(1)).to_have_text(
                "Powered by Sertis"
            )
        except Exception as e:
            pytest.fail(f"Element presence check failed: {e}")

    def _pre_signin(self, email=None, password=None):
        if email is None or email == "correct":
            email = self.BASE_EMAIL
        if password is None or password == "correct":
            password = self.BASE_PASSWORD

        self.page.goto(self.BASE_URL + "/")
        self.elem("email_input").fill(email)
        self.elem("password_input").fill(password)

    def signin(self):
        self._pre_signin()
        show_password_checkbox = self.elem("show_password_checkbox")
        show_password_checkbox.click()
        expect(self.elem("password_input")).to_have_attribute("type", "text")
        show_password_checkbox.click()
        expect(self.elem("password_input")).to_have_attribute("type", "password")

        self.elem("signin_button").click()
        expect(self.page).to_have_url(
            self.BASE_URL + "/en/platform/reports", timeout=10000
        )

    def signin_invalid(self, email, password):
        assert not (
            email == "correct" and password == "correct"
        ), "Email and password should not be both correct for this test."

        self._pre_signin(email, password)
        self.elem("signin_button").click()

        if not email:
            expect(self.elem("email_input_error_label")).to_have_text(
                "Please enter your email before continuing."
            )
        if not password:
            expect(self.elem("password_input_error_label")).to_have_text(
                "Please enter your password before continuing."
            )

        if email and password:
            expect(self.elem("email_input_error_label")).to_have_text(
                "Email or password is incorrect. Please try again."
            )
            expect(self.elem("password_input_error_label")).to_have_text(
                "Email or password is incorrect. Please try again."
            )

    def signin_refresh(self):
        self._pre_signin()
        self.page.reload()
        expect(self.elem("email_input")).to_be_visible()
        expect(self.elem("email_input")).to_have_attribute(
            "placeholder", "Enter your email"
        )
        expect(self.elem("password_input")).to_have_attribute(
            "placeholder", "Enter your password"
        )
    
    def check_loading_page(self):
        self._pre_signin()
        self.elem("signin_button").click()
        expect(self.elem("loading")).to_be_visible(timeout=3000)
        expect(self.elem("spinner")).to_be_visible(timeout=3000)

    def check_device_not_supported(self, width=800, height=800):
        self.page.set_viewport_size({"width": width, "height": height})
        self.page.goto(self.BASE_URL + "/")
        expect(self.elem("logo_unsupported")).to_be_visible()
        expect(self.elem("title")).to_have_text("Device not supported")
        expect(self.elem("subtitle")).to_have_text(
            "This device does not meet our requirements. For a better experience, please try again on a different device or contact support for assistance."
        )
        expect(self.elem("contact_email_unsupported")).to_be_visible()
        time.sleep(1)

    def check_mail_link_open(self):
        self.page.goto(self.BASE_URL + "/")
        mail_link = self.elem("contact_us_link").locator("a").first
        display_mail = mail_link.text_content()
        expect(mail_link).to_have_attribute("href", f"mailto:{display_mail}")