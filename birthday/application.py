from tornado.web import Application

from birthday import config

def make_app():
    handlers = []

    settings = {
        "debug": config.DEBUG
    }
    return Application(handlers, **settings)