import os
from dotenv import load_dotenv
import pytest
import time
from playwright.sync_api import Page, expect
import logging
from utils import retention_date_format
from data.supplier_form_data import form_data
from locator import locators, errors

load_dotenv()
retailer_email = os.getenv("RETAILER_EMAIL", "")
retailer_password = os.getenv("RETAILER_PASSWORD", "")
otp_code = os.getenv("OTP_CODE", "")
base_url = os.getenv("BASE_URL", "")

logger = logging.getLogger("logger")

@pytest.fixture(autouse=True)
def enter_site(page: Page):
    page.goto(base_url)

    page.locator(locators["email_input"]).fill(retailer_email)
    page.locator(locators["password_input"]).fill(retailer_password)

    page.locator(locators["sign_in_button"]).click()

    try:
        otp_input = page.locator(locators["otp_input"])
        otp_input.wait_for(timeout=3000)
        otp_input.fill(otp_code)
        page.locator(locators["verify_button"]).click()
        logger.info("OTP code entered successfully.")
    except:
        logger.info("No OTP input found, proceeding without entering OTP.")

    page.wait_for_url(base_url + "/en/platform/reports")
    page.goto(base_url + "/en/platform/suppliers")
    page.wait_for_load_state("domcontentloaded")


@pytest.mark.skip(reason="Skipping test for now.")
@pytest.mark.parametrize("data", form_data)
def test_supplier_form(page: Page, data):
    supplier_name = data["supplier_name"]
    business_type = data["business_type"]
    end_date = data["end_date"]
    retention_days = data["retention_days"]

    page.locator(locators["test_row"]).click()
    page.wait_for_load_state("domcontentloaded")

    page.locator(locators["edit_button"]).click()
    page.wait_for_load_state("domcontentloaded")

    page.locator(locators["supplier_name_input"]).fill(supplier_name)
    page.locator(locators["business_type_input"]).fill(business_type)
    page.locator(locators["retention_days_input"]).fill(retention_days)
    page.locator(locators["date_picker_range"]).nth(1).click()
    page.locator(locators["date_picker_cell"].format(date=end_date)).click()

    start_date_value = page.locator(locators["date_picker_range"]).nth(0).input_value()
    end_date_value = page.locator(locators["date_picker_range"]).nth(1).input_value()

    error_found = False
    for key, error in errors.items():
        try:
            error_element = page.locator(error["path"])
            error_element.wait_for(timeout=1000)
            expect(error_element).to_have_text(error["message"])
            error_found = True
            logger.info(f"{key} - {error['message']}")
        except:
            logger.info(f"{key} not present")

    if error_found:
        return

    page.locator(locators["save_button"]).click()

    expect(
        page.get_by_test_id(
            "supplier-detail-content-test-id-general_info-item-0-content"
        )
    ).to_have_text(supplier_name)
    expect(
        page.get_by_test_id(
            "supplier-detail-content-test-id-general_info-item-1-content"
        )
    ).to_have_text(business_type)
    expect(
        page.get_by_test_id(
            "supplier-detail-content-test-id-general_info-item-2-content"
        )
    ).to_have_text(start_date_value + " - " + end_date_value)
    expect(
        page.get_by_test_id(
            "supplier-detail-content-test-id-general_info-item-3-content"
        )
    ).to_have_text(retention_date_format(end_date, retention_days))
