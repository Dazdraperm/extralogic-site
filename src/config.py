"""App Config"""


class Config(object):
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True


class DevConfig(Config):
    # SQLALCHEMY_ECHO = True
    DEBUG = True


""""""
