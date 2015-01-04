from flask import Flask

from . import views

def create_app(**config):
  app = Flask(__name__)
  app.config.update(**config)
  app.register_blueprint(views.bp)
  return app