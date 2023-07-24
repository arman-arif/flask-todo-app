from flask_migrate import Migrate

from app.routes.web import Route
from app.app import app
from app.db import db

migrate = Migrate(app, db)

blueprint = Route.blueprint()

app.register_blueprint(blueprint, url_prefix='/')
