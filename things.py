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


class Hello(object):
    def do_something(req, resp, resource, params):
        try:
            print(params['num'])
        except ValueError:
            raise falcon.HTTPBadRequest('Invalid ID',
                                        'ID was not valid.')

    @falcon.before(do_something)
    def on_get(self, req, resp, num):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = "hello" + str(num)
        print("hi")





app = falcon.API()

hello = Hello()

app.add_route('/hello/{num}', hello)
