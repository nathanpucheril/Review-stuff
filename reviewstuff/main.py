from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from reviewstuff import routes
import os


# create the extension
db = SQLAlchemy()


def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))

    # create the app
    app = Flask(__name__, instance_relative_config=False)

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, '../database/app.db')

    db.init_app(app)

    routes.routes(app, db)

    app.db = db

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
