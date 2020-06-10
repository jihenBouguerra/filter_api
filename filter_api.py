# class test():
#     def __init__(self):
#         self.test_first_Query()
#
#     def first_query(self):
#         return
#
#     def second_query(self):
#         return
#
#     def third_query(self):
#         return
#     def fourth_query(self):
#         return
#
#
import falcon
import numpy as np

from api_utils import *
from request_business import RequestBusiness
from config import Configuration


class FilterAPI(object):

    def do_control(req, resp, resource, params):
        try:
            if [x for x in req.params if x not in Configuration.filter_names]:
                raise ValueError()
            # map request params
            countries = get_value_or_default(req.params, "countries", [], string_to_array)
            channels = get_value_or_default(req.params, "channels", [], string_to_array)
            display = get_value_or_default(req.params, "display", [], string_to_array)
            os = get_value_or_default(req.params, "os", [], string_to_array)
            group_by = get_value_or_default(req.params, "group_by", [], string_to_array)
            inc = get_value_or_default(obj=req.params, key="inc", map_function=string_to_boolean)
            start_date = get_value_or_default(req.params, "start_date", Configuration.min_date, string_to_date)
            end_date = get_value_or_default(req.params, "end_date", Configuration.max_date, string_to_date)
            order_by = get_value_or_default(req.params, "order_by", [], string_to_date)

            # print(countries, channels,display,os,group_by,inc,start_date,end_date)
            request = RequestBusiness(countries=countries, display=display, channels=channels,
                                      operating_systems=os, inc=inc, start_date=start_date, end_date=end_date,
                                      group_by=group_by, order_by=order_by)
            if not request.valid:
                raise ValueError()
            req.context = request

        except ValueError:
            raise falcon.HTTPBadRequest('Invalid query',
                                        'query was not valid.')

    @falcon.before(do_control)
    def on_get(self, req, resp):
        # print(req.context.countries)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = req.context.result.to_json(orient='records')

        # print(filter)


app = falcon.API()

filter_api = FilterAPI()

app.add_route('/api/filter', filter_api)
# app.add_route('/api/filter/{filter}', filter_api)
