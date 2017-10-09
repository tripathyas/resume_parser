import re
import logging


class ParamRegexMap():

    param_list = ["phone_number", "email"]

    @staticmethod
    def check_phone_number(string_to_search):
        try:
            regular_expression = re.compile(r"\(?"  # open parenthesis
                                            r"(\d{3})?"  # area code
                                            r"\)?"  # close parenthesis
                                            # area code, phone separator
                                            r"[\s\.-]{0,2}?"
                                            r"(\d{3})"  # 3 digit exchange
                                            # separator bbetween 3 digit exchange, 4 digit local
                                            r"[\s\.-]{0,2}"
                                            r"(\d{4})",  # 4 digit local
                                            re.IGNORECASE)
            result = re.search(regular_expression, string_to_search)
            if result:
                result = result.groups()
                result = "-".join(result)
            return result
        except Exception as exception_instance:
            logging.error('Issue parsing phone number: ' +
                          string_to_search + str(exception_instance))
            return None

    @staticmethod
    def check_email(string_to_search):
        try:
            regular_expression = re.compile(
                r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
            result = re.search(regular_expression, string_to_search)
            if result:
                result = result.group()
            return result
        except Exception as exception_instance:
            logging.error('Issue parsing email number: ' +
                          string_to_search + str(exception_instance))
            return None

    def __init__(self):
        pass
