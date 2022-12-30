from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from reviewstuff import routes
from reviewstuff.config.config import Config
from flask.json import JSONEncoder
from contextlib import suppress

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        # Optional: convert datetime objects to ISO format
        with suppress(AttributeError):
            return obj.isoformat()
        return dict(obj)


def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    cfg = Config(basedir)

    # create the app
    flask_app = Flask(__name__, instance_relative_config=False)

    # configure the SQLite database, relative to the app instance folder
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = cfg.SQLALCHEMY_DATABASE_URI

    # create the extension
    db = SQLAlchemy(flask_app)

    routes.routes(flask_app, db)

    flask_app.json_encoder = MyJSONEncoder
    flask_app.db = db
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
