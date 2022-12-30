import os


class Config(object):

    def __init__(self, basedir):
        self.basedir = basedir

        # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
        # update the URI to the postgres database to use the supported 'postgresql://' scheme
        if os.getenv('DATABASE_URL'):
            self.SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
        else:
            self.SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'database', 'app.db')}"


