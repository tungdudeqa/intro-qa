invalid_form_data = [
    {
        "supplier_name": "",
        "business_type": "DEF",
        "end_date": "2025-12-07",
        "retention_days": "3",
    },
    {
        "supplier_name": "TEST SUPPLIER 3",
        "business_type": "123",
        "end_date": "2025-12-14",
        "retention_days": "5",
    },
    {
        "supplier_name": "TEST SUPPLIER 4",
        "business_type": "JKL",
        "end_date": "2025-12-21",
        "retention_days": "",
    },
]

valid_form_data = [
    {
        "supplier_name": "TEST SUPPLIER 1",
        "business_type": "ABC",
        "end_date": "2026-12-01",
        "retention_days": "1",
    },
    {
        "supplier_name": "TEST SUPPLIER 2",
        "business_type": "ABC",
        "end_date": "2026-02-01",
        "retention_days": "1",
    },
    {
        "supplier_name": "TEST SUPPLIER 3",
        "business_type": "ABC",
        "end_date": "2025-09-07",
        "retention_days": "1",
    },
]

date_data = [
    "2024-01-05",
    "2025-02-02",
    "2025-12-02",
    "2026-12-04",
    "2026-02-01",
]