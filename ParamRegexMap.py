import re


class ParamRegexMap():
    
    param_regex_match = {
        'address': re.compile(r"[0-9]+ [a-z0-9,\.# ]+\bCA\b", re.IGNORECASE),
        'email': re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE),
        'contact_number': re.compile(r"\(?"  # open parenthesis
                                     r"(\d{3})?"  # area code
                                     r"\)?"  # close parenthesis
                                     # area code, phone separator
                                     r"[\s\.-]{0,2}?"
                                     r"(\d{3})"  # 3 digit exchange
                                     # separator bbetween 3 digit exchange, 4 digit local
                                     r"[\s\.-]{0,2}"
                                     r"(\d{4})",  # 4 digit local
                                     re.IGNORECASE)
    }

    def __init__(self):
        pass
