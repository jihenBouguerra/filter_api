from datetime import datetime


class Configuration:
    group_by_columns = ["date", "channel", "country", "os"]
    sum_columns = ["installs", "spend", "revenue", "cpi"]
    filter_names = ["countries", "channels", "display", "os", "start_date", "end_date", "group_by", "inc", "order_by","sum"]
    data_path = "dataset.csv"
    min_date = datetime(1973, 1, 1)
    max_date = datetime.now()

    @staticmethod
    def date_range(): return Configuration.min_date, Configuration.max_date
