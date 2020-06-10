from datetime import datetime


def default_map_function(element):
    return element


def string_to_array(str="[]", split_char=","):
    return [element for element in str[1:][:-1].split(split_char) if element]


def string_to_boolean(str="False"):
    return True if str.lower() in ("true", "1", "t") else False


def string_to_date(str="1973-01-01"):
    return datetime.strptime(str, "%Y-%m-%d")


def get_value_or_default(obj={}, key="", default="", map_function=default_map_function):
    return map_function(obj[key]) if key in obj else default
