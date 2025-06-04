locators = {
    "email_input": 'xpath=//*[@data-testid="email-input"]',
    "password_input": 'xpath=//*[@data-testid="password-input"]',
    "sign_in_button": 'xpath=//button[normalize-space(text())="Sign in"]',
    "otp_input": 'xpath=//*[@data-testid="otp-input"]',
    "verify_button": 'xpath=//button[@data-testid="submit-btn"]',
    "test_row": 'xpath=//*[@data-testid="undefined-body-row-0"]',
    "edit_button": 'xpath=//button[normalize-space(text())="Edit"]',
    "supplier_name_input": 'xpath=//*[@data-testid="genInfo.name-text-input-id"]',
    "business_type_input": 'xpath=//*[@data-testid="genInfo.businessType-text-input-id"]',
    "retention_days_input": 'xpath=//*[@data-testid="genInfo.retentionDays-text-input-id"]',
    "date_picker_range": 'xpath=//*[@data-testid="date-picker-range-test-id"]',
    "date_picker_cell": 'xpath=//td[contains(@class, "ant-picker-cell-in-view") and @title="{date}"]',
    "save_button": 'xpath=//button[normalize-space(text())="Save"]',
}

errors = {
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
