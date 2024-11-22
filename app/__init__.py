from flask import Flask

def create_app():
  app = Flask(__name__)

  from .views.main_views import main
  from .views.about_views import about

  app.register_blueprint(main)
  app.register_blueprint(about)

  return app