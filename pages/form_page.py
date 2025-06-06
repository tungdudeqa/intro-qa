from pages.signin_page import SigninPage
from playwright.sync_api import expect
from utils import retention_date_format
from datetime import datetime as dt
from utils import month_abbr_to_num
import time


class FormPage(SigninPage):
    def __init__(self, page):
        super().__init__(page)
        self.locators.update(
            {
                "test_row": '//*[@data-testid="undefined-body-row-0"]',
                "form_edit_button": '//button[normalize-space(text())="Edit"]',
                "supplier_name_input": '//*[@data-testid="genInfo.name-text-input-id"]',
                "business_type_input": '//*[@data-testid="genInfo.businessType-text-input-id"]',
                "retention_days_input": '//*[@data-testid="genInfo.retentionDays-text-input-id"]',
                "date_picker_range": '//*[@data-testid="date-picker-range-test-id"]',
                "date_picker_cell": '//td[contains(@class, "ant-picker-cell-in-view") and @title="{date}"]',
                "save_button": '//button[normalize-space(text())="Save"]',
                "supplier_name_display": '//*[@data-testid="supplier-detail-content-test-id-general_info-item-0-content"]',
                "business_type_display": '//*[@data-testid="supplier-detail-content-test-id-general_info-item-1-content"]',
                "start_date_display": '//*[@data-testid="supplier-detail-content-test-id-general_info-item-2-content"]',
                "retention_date_display": '//*[@data-testid="supplier-detail-content-test-id-general_info-item-3-content"]',
                "calendar_month_btn": '//button[@class="ant-picker-month-btn"]',
                "calendar_month_option": '//td[contains(@class, "ant-picker-cell-in-view") and .//div[text()="{short_month}"]]',
                "calendar_year_btn": '//button[@class="ant-picker-year-btn"]',
                "calendar_year_option": '//td[contains(@class, "ant-picker-cell-in-view") and .//div[text()="{year}"]]',
                "contract_date_details": '//body/div/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/h5',
            }
        )
        self.errors = {
            "supplier_error": {
                "path": 'xpath=//label[@data-testid="genInfo.name-text-input-id-error-label"]',
                "message": "Please enter your supplier name before continuing.",
            },
            "business_type_error": {
                "path": 'xpath=//label[@data-testid="genInfo.businessType-text-input-id-error-label"]',
                "message": "This field can only contain alphabetic characters (A-Z, a-z).",
            },
            "retention_days_error": {
                "path": 'xpath=//label[@data-testid="genInfo.retentionDays-text-input-id-error-label"]',
                "message": "Please enter the number of retention days before continuing.",
            },
        }

    def _goto(self):
        self.signin()
        self.goto("/en/platform/suppliers")
        self.page.wait_for_load_state("domcontentloaded")

    def _select_supplier(self, edit=False):
        self.elem("test_row").click()
        self.page.wait_for_load_state("domcontentloaded")
        if edit:
            self.elem("form_edit_button").click()
            self.page.wait_for_load_state("domcontentloaded")

    def check_valid_input_save(
        self, supplier_name, business_type, retention_days, end_date
    ):
        self._goto()
        self._select_supplier(edit=True)
        self.elem("supplier_name_input").fill(supplier_name)
        self.elem("business_type_input").fill(business_type)
        self.elem("retention_days_input").fill(retention_days)
        self.elem("date_picker_range").nth(1).click()

        year, short_month = dt.strptime(end_date, "%Y-%m-%d").strftime("%Y %b").split()

        #pick year
        self.elem("calendar_year_btn").nth(1).click()
        year_option = self.elem("calendar_year_option", year=year)
        year_option.click()

        # pick month
        month_option = self.elem("calendar_month_option", short_month=short_month)
        month_option.click()

        self.elem("date_picker_cell", date=end_date).click()

        start_date_value = self.elem("date_picker_range").nth(0).input_value()
        end_date_value = self.elem("date_picker_range").nth(1).input_value()

        self.elem("save_button").click()

        supplier_name_display = self.elem("supplier_name_display")
        business_type_display = self.elem("business_type_display")
        start_date_display = self.elem("start_date_display")
        retention_date_display = self.elem("retention_date_display")

        self.logger.info("Checking saved values:")
        self.logger.info(f"Expected supplier Name: {supplier_name}")
        self.logger.info(f"Expected business Type: {business_type}")
        self.logger.info(f"Expected retention Days: {retention_days}")
        self.logger.info(f"Expected start Date: {start_date_value + " - " + end_date_value}")
        self.logger.info(f"Expected retention Date: {retention_date_format(end_date, retention_days)}")

        expect(supplier_name_display).to_have_text(supplier_name)
        expect(business_type_display).to_have_text(business_type)
        expect(start_date_display).to_have_text(
            start_date_value + " - " + end_date_value
        )
        expect(retention_date_display).to_have_text(
            retention_date_format(end_date, retention_days)
        )

    def check_invalid_input(self, supplier_name, business_type, retention_days):
        self._goto()
        self._select_supplier(edit=True)
        self.elem("supplier_name_input").fill(supplier_name)
        self.elem("business_type_input").fill(business_type)
        self.elem("retention_days_input").fill(retention_days)

        error_found = False
        for key, error in self.errors.items():
            try:
                error_element = self.page.locator(error["path"])
                error_element.wait_for(timeout=1000)
                expect(error_element).to_have_text(error["message"])
                error_found = True
                self.logger.info(f"{key} - {error['message']}")
            except:
                self.logger.info(f"{key} not present")

        if not error_found:
            raise AssertionError("No errors found when expected.")
    
    def validate_end_date(self, end_date):
        self._goto()
        self.goto("/en/platform/information")

        contract_end_date = self.elem("contract_date_details").text_content().split("-")[1].strip()
        contract_end_dt = dt.strptime(contract_end_date, "%d %b %Y")
        end_date_dt = dt.strptime(end_date, "%Y-%m-%d")
        today = dt.today()
        curr_year, curr_month = today.strftime("%Y %b").split()

        self.goto("/en/platform/suppliers")
        self._select_supplier(edit=True)

        self.elem("date_picker_range").nth(1).click()

        year, short_month = dt.strptime(end_date, "%Y-%m-%d").strftime("%Y %b").split()

        #pick year
        self.elem("calendar_year_btn").nth(1).click()
        year_option = self.elem("calendar_year_option", year=year)
        if int(year) < int(curr_year):
            self.logger.info(f"Year {year} is less than current year {curr_year}. Expect disabled year option.")
            expect(year_option).to_contain_class("ant-picker-cell-disabled")
            return
        year_option.click()

        # pick month
        month_option = self.elem("calendar_month_option", short_month=short_month)
        if int(year) == int(curr_year) and month_abbr_to_num(short_month) < month_abbr_to_num(curr_month):
            self.logger.info(f"Month {short_month} is less than current month {curr_month} in the same year. Expect disabled month option.")
            expect(month_option).to_contain_class("ant-picker-cell-disabled")
            return
        month_option.click()

        if end_date_dt <= contract_end_dt and end_date_dt > today:
            self.logger.info(f"End date {end_date} is within the contract period and after today. Expect enabled option.")
            expect(self.elem("date_picker_cell", date=end_date)).not_to_contain_class("ant-picker-cell-disabled")
        else:
            self.logger.info(f"End date {end_date} is outside the contract period or before today. Expect disabled option.")
            expect(self.elem("date_picker_cell", date=end_date)).to_contain_class("ant-picker-cell-disabled")
