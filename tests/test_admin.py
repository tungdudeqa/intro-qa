from pages.admin_page import AdminPage
from playwright.sync_api import Page
from data.admin_form_data import first_name_data, last_name_data, email_data, phone_data
import pytest

test_data_error_field = [
    *[{
        "field": "first_name",
        "value": value,
    } for value in first_name_data],
    *[{
        "field": "last_name",
        "value": value,
    } for value in last_name_data],
    *[{
        "field": "email",
        "value": value,
    } for value in email_data],
    *[{
        "field": "phone",
        "value": value,
    } for value in phone_data],
]

# some phone numbers are not valid, but the web does not show error message because of the validator lib used to dev
@pytest.mark.parametrize("obj", test_data_error_field, ids=[f"{f}-{v}" for f, v in test_data_error_field])
def test_input_field_error_messages(page: Page, obj):
    admin_page = AdminPage(page)
    admin_page.check_error_message(obj["field"], obj["value"])