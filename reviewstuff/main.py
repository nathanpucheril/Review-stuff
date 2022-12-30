from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from reviewstuff import routes
from reviewstuff.config.config import Config

load_dotenv()


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

    flask_app.db = db
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
