from handlers.base_handler import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
