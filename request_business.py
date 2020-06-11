from pandas import read_csv, to_datetime, Series, DataFrame

from api_utils import string_to_date
from config import Configuration
import falcon


class RequestBusiness(falcon.Request):
    df_data = {}

    @staticmethod
    def load_data():
        if len(RequestBusiness.df_data) == 0:
            df = read_csv(Configuration.data_path)
            df.date = to_datetime(df.date)
            df["cpi"] = Series(df.spend / df.installs)
            RequestBusiness.df_data = df
        return RequestBusiness.df_data

    def __init__(self, countries=[], operating_systems=[], channels=[], inc=False, group_by=[], display=[],
                 start_date=Configuration.min_date, end_date=Configuration.max_date, order_by=[], sum_=[]):
        self.df = RequestBusiness.load_data()
        self.countries = countries
        self.start_date = start_date
        self.end_date = end_date
        self.operating_systems = operating_systems
        self.channels = channels
        self.inc = inc
        self.sum_ = sum_
        self.group_by = group_by
        self.display = display
        self.order_by = order_by
        self.valid = self.control_request()
        print(self.valid)
        self.result = self.filter_data()

    def filter_data(self):
        result = DataFrame()
        if self.valid:
            result = self.df.copy()
            if self.start_date:
                result = result[result['date'].notnull() & (self.start_date <= result['date'])]
            if self.end_date:
                result = result[result['date'].notnull() & (result['date'] <= self.end_date)]
            if len(self.channels) > 0:
                result = result[result['channel'].notnull() & (result["channel"].isin(self.channels))]
            if len(self.operating_systems) > 0:
                result = result[result["os"].notnull() & result["os"].isin(self.operating_systems)]
            if len(self.countries) > 0:
                result = result[result["country"].notnull() & result["country"].isin(self.countries)]

            if len(self.sum_) > 0 and len(self.group_by) > 0:
                result = result.groupby(self.group_by)[self.sum_].sum().reset_index()
            if len(self.order_by) > 0:
                result = result.sort_values(by=self.order_by, ascending=self.inc)
            if len(self.display) > 0:
                result = result[self.display]

        return result

    def control_request(self):
        start_dt, end_dt = Configuration.date_range()
        if self.end_date > end_dt or self.end_date < start_dt:
            return False
        if self.start_date > end_dt or self.start_date < start_dt:
            return False
        if self.start_date > self.end_date:
            return False
        for g_b in self.group_by:
            if g_b not in Configuration.group_by_columns:
                return False
        for o_b in self.order_by:
            if o_b not in self.df.columns:
                return False
        for s_c in self.sum_:
            if s_c not in Configuration.sum_columns or len(self.group_by) == 0:
                return False
        for d in self.display:
            if d not in self.df.columns:
                return False
        return True

