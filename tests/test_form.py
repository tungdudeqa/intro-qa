from dotenv import load_dotenv
import pytest
import time
from playwright.sync_api import Page
from utils import retention_date_format
from data.supplier_form_data import valid_form_data, invalid_form_data, date_data
from pages.form_page import FormPage

load_dotenv()

@pytest.mark.skip(reason="Skipping test for now.")
@pytest.mark.parametrize("data", valid_form_data)
def test_valid_supplier_form(page: Page, data):
    form_page = FormPage(page)
    form_page.check_valid_input_save(
        supplier_name=data["supplier_name"],
        business_type=data["business_type"],
        retention_days=data["retention_days"],
        end_date=data["end_date"],
    )

@pytest.mark.skip(reason="Skipping test for now.")
@pytest.mark.parametrize("data", invalid_form_data)
def test_invalid_supplier_form(page: Page, data):
    form_page = FormPage(page)
    form_page.check_invalid_input(
        supplier_name=data["supplier_name"],
        business_type=data["business_type"],
        retention_days=data["retention_days"],
    )

@pytest.mark.skip(reason="Skipping test for now.")
@pytest.mark.parametrize("date", date_data)
def test_validate_date(page: Page, date):
    form_page = FormPage(page)
    form_page.validate_end_date(date)