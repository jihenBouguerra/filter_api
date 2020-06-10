import falcon

from request import Request


class Response:
    def __init__(self):
        self.body = ""
        self.status = None


class FilterAPI:
    def on_get(self, rest, resp, msg):
        # rest = request.df.copy()
        # if request.valid:
        #     if request.start_date:
        #         rest = rest[rest['date'].notnull() & (request.start_date < rest['date'])]
        #     if request.end_date:
        #         rest = rest[rest['date'].notnull() & (rest['date'] < request.end_date)]
        #     if request.channels and len(request.channels) != 0:
        #         rest = rest[rest['channel'].notnull() & (rest["channel"].isin(request.channels))]
        #     if request.operating_systems and len(request.operating_systems) != 0:
        #         rest = rest[rest["os"].notnull() & rest["os"].isin(request.operating_systems)]
        #     if len(request.countries) != 0:
        #         rest = rest[rest["country"].notnull() & rest["country"].isin(request.countries)]
        #     if request.group_by:
        #         rest.sort_values(by=request.group_by, ascending=request.inc)
        #     if 0 < len(request.display):
        #         rest = rest[request.display]
        # resp.body = rest
        # print(resp.body)
        print(msg)
        resp.status = falcon.HTTP_200


api = falcon.API()
request = Request(countries=["FR", "DE"], display=["channel", "cpi", "country", "os"], channels=[],
                  operating_systems=["ios"])
msg="hi"
api.add_route('/filter/{msg}', FilterAPI())
