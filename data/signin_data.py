dcp_signin_data = {
    "special_characters": "!@#$%^&*()_+{}|:\"<>?[];',./`~",
    "wrong": "test@mail.com",
    "english": "cv akdkwqk d ksamdk qow ",
    "thai": "ๆไยำมสแอมยๆไ๑๗๒๓๗๘+๗๘ฆ ศฒฉฤฆฤฆฬฏญ๐วฟหก",
    "space": " ",
    "unicode": "オラオラオラオラオラオラオラオラオラ🤯🤗🥰😃😋😚😐😶😏😏🤗😣😏😶",
    "sql_injection": "' OR '1'='1",
    "xss": "<script>alert(1)</script>",
    "format_string_injection": "%s@example.com",
    "css_injection": "<style>body{ display : none; }</style>",
    "nosql_injection": '{ "$ne": null }',
    "super_long": "a" * 999999 + "!",
}