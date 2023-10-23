class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, route_cls):
        self.path = path
        self.route_cls = route_cls

    def __call__(self, func):
        self.route_cls.get(self.path, func)