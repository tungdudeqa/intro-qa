first_name_data = [
    "",
    "123",
    "😍",
    "สฟหากนานๆไ",
]

last_name_data = [
    "",
    "123",
    "😍",
    "สฟหากนานๆไ",
]

email_data = [
    "",
    "invalid-email",
    "user@domain",
    "ฟกกsdsหก.com",
]

phone_data = [
    "",
    "1234567890", # should not pass test
    "829392021", # should not pass test
    "0093334134", # should pass test
    "0012348585949300", # should pass test
    "0093294958304", # should pass test
    "00123485859493002132", # should pass test
]