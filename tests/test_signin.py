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

@pytest.mark.skip(reason="done in test_dcp_005")
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

@pytest.mark.skip(reason="done in test_dcp_007")
def test_dcp_007(page: Page):
    signin_page = SigninPage(page)
    signin_page.signin_invalid(email="", password="password")

@pytest.mark.skip(reason="done in test_dcp_008")
def test_dcp_008(page: Page):
    signin_page = SigninPage(page)
    signin_page.signin_invalid(email="email", password="")

# error right now - the web only shows email error message
@pytest.mark.skip(reason="error right now - the web only shows email error message")
def test_dcp_009(page: Page):
    signin_page = SigninPage(page)
    signin_page.signin_invalid(email="", password="")

@pytest.mark.skip(reason="done in test_dcp_010")
def test_dcp_010(page: Page):
    signin_page = SigninPage(page)
    signin_page.signin_refresh()

@pytest.mark.skip(reason="done in test_dcp_012")
def test_dcp_012(page: Page):
    signin_page = SigninPage(page)
    signin_page.goto("/index")
    signin_page.check_elements_presence()

@pytest.mark.skip(reason="done in test_dcp_013")
def test_dcp_013(page: Page):
    signin_page = SigninPage(page)
    signin_page.check_loading_page()

@pytest.mark.skip(reason="done in test_dcp_018")
def test_dcp_018(page: Page):
    signin_page = SigninPage(page)
    signin_page.check_device_not_supported()