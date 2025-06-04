from playwright.sync_api import Page
from pages.signin_page import SigninPage
from data.signin_data import dcp_signin_data
import pytest

@pytest.mark.skip(reason="done in test_dcp_001")
def test_dcp_001(page: Page):
    signin_page = SigninPage(page)
    signin_page.check_elements_presence()

@pytest.mark.skip(reason="done in test_dcp_003")
def test_dcp_003(page: Page):
    signin_page = SigninPage(page)
    signin_page.check_elements_presence()
    signin_page.signin()

@pytest.mark.skip(reason="done in test_dcp_004")
@pytest.mark.parametrize("password", dcp_signin_data.values(), ids=dcp_signin_data.keys())
def test_dcp_004(page: Page, password):
    signin_page = SigninPage(page)
    signin_page.signin_invalid(email="correct", password=password)

@pytest.mark.parametrize("value", dcp_signin_data.values(), ids=dcp_signin_data.keys())
def test_dcp_005(page: Page, value):
    signin_page = SigninPage(page)
    signin_page.check_elements_presence()
    signin_page.signin_invalid(email=value, password=value)

@pytest.mark.skip(reason="done in test_dcp_006")
@pytest.mark.parametrize("email", dcp_signin_data.values(), ids=dcp_signin_data.keys())
def test_dcp_006(page: Page, email):
    signin_page = SigninPage(page)
    signin_page.check_elements_presence()
    signin_page.signin_invalid(email=email, password="correct")