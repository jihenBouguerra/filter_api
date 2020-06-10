from datetime import datetime


def group_by_col(): return ["date", "channel", "country", "os"]


def date_range(): return datetime(2000, 12, 20), datetime(2030, 1, 11)


def data_path(): return "dataset.csv"
