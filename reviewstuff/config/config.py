import os
import yaml
from dotenv import load_dotenv

ENV_PRODUCTION = "production"
ENV_LOCAL = "local"


class Config(object):

    def __init__(self, basedir):
        self.basedir = basedir
        print("basedir: " + basedir)
        load_dotenv()

        self.env = os.getenv("ENV")
        print(self.env)

        config_env_file_name = \
            'local' if self.env == ENV_LOCAL else \
            'production' if self.env == ENV_PRODUCTION else \
            None

        with open(f'{basedir}/config/{config_env_file_name}.yaml', 'r') as file:
            config_yaml = yaml.safe_load(file)

        secrets_path = f"{os.path.join(self.basedir, config_yaml['secrets']['env_file_path'])}"
        load_dotenv(secrets_path)

        # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
        # update the URI to the postgres database to use the supported 'postgresql://' scheme
        main_db_config = config_yaml["database"]["main"]
        self.SQLALCHEMY_DATABASE_URI = self.__get_sqlalchemy_db_uri(main_db_config)

    def __get_sqlalchemy_db_uri(self, db_config):
        type_ = db_config['type']
        if type_ == 'postgres':
            username = db_config['username']
            host = db_config['host']
            database = db_config['database']
            password = os.getenv(db_config['password'])
            return f'postgresql://{username}:{password}@{host}/{database}'
        elif type_ == 'sqlite':
            path_ext = db_config['path_ext']
            return f"sqlite:///{os.path.join(self.basedir, path_ext)}"
