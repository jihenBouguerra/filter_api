from pandas import read_csv, to_datetime, Series

from api_utils import date_range, data_path, group_by_col, datetime
import falcon


class Request(falcon.Request):
    @staticmethod
    def load_data():
        df = read_csv(data_path())
        df.date = to_datetime(df.date)
        df["cpi"] = Series(df.spend / df.installs)
        return df

    def __init__(self, countries=[], operating_systems=[], channels=[], inc=False, group_by=[], display=[],
                 start_date=datetime(2013, 12, 29), end_date=datetime(2017, 12, 29)):
        self.df = self.load_data()
        self.countries = countries
        self.start_date = start_date
        self.end_date = end_date
        self.operating_systems = operating_systems
        self.channels = channels
        self.inc = inc
        self.group_by = group_by
        self.display = display
        self.valid = self.control_request()

    def control_request(self):
        start_dt, end_dt = date_range()
        if self.end_date > end_dt or self.end_date < start_dt:
            return False
        if self.start_date > end_dt or self.start_date < start_dt:
            return False
        for g_b in self.group_by:
            if g_b not in group_by_col():
                return False
        for d in self.display:
            if d not in self.df.columns:
                return False
        for country in self.countries:
            if country not in self.df.country.values:
                return False
        for os in self.operating_systems:
            if os not in self.df.os.values:
                return False
        for channel in self.channels:
            if channel not in self.df.channel.values:
                return False
        return True
