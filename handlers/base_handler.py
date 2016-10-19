import tornado.web
from utils.web_utils import decode_body


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.json_args = None

    def prepare(self):
        if self.request.headers["Content-Type"].startswith("application/json"):
            self.json_args = decode_body(self.request.body)

    def data_received(self, chunk):
        pass
