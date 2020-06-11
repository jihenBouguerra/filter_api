import falcon
from api_utils import *
from request_business import RequestBusiness
from config import Configuration


class FilterAPI(object):
    def do_control(req, resp, resource, params):


        try:
            if [x for x in req.params if x not in Configuration.filter_names]:
                print("name parameter incorrect")
                raise ValueError()

            countries = get_value_or_default(req.params, "countries", [], string_to_array)
            channels = get_value_or_default(req.params, "channels", [], string_to_array)
            display = get_value_or_default(req.params, "display", [], string_to_array)
            sum_ = get_value_or_default(req.params, "sum", [], string_to_array)
            os = get_value_or_default(req.params, "os", [], string_to_array)
            group_by = get_value_or_default(req.params, "group_by", [], string_to_array)
            inc = get_value_or_default(obj=req.params, key="inc", map_function=string_to_boolean)
            start_date = get_value_or_default(req.params, "start_date", Configuration.min_date, string_to_date)
            end_date = get_value_or_default(req.params, "end_date", Configuration.max_date, string_to_date)
            order_by = get_value_or_default(req.params, "order_by", [], string_to_array)
            # print(countries, channels,display,os,group_by,inc,start_date,end_date)
            request = RequestBusiness(countries=countries, display=display, channels=channels,
                                      operating_systems=os, inc=inc, start_date=start_date,
                                      end_date=end_date, group_by=group_by, order_by=order_by, sum_=sum_)
            print(request.valid)
            if not request.valid:
                print("query incorrect")
                raise ValueError()
            req.context = request
        except ValueError:
            raise falcon.HTTPBadRequest('Invalid query',
                                        'query was not valid.')

    @falcon.before(do_control)
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        resp.body = req.context.result.to_json(orient='records',date_format='iso')


app = falcon.API()
filter_api = FilterAPI()
app.add_route('/api/filter', filter_api)
