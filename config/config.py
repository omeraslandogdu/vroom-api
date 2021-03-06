import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = False
    TESTING = False
    TESTS_FOLDER = 'tests'
    LOGGING_LEVEL = 'DEBUG'
    HOST = '0.0.0.0'
    PORT = 1881

    def __init__(self):
        if os.getenv('PORT'):
            Config.PORT = os.getenv('PORT')
        if os.getenv('HOST'):
            Config.HOST = os.getenv('HOST')
        if os.getenv('LOGGING_LEVEL'):
            Config.LOGGING_LEVEL = os.getenv('LOGGING_LEVEL')


class ProductionConfig(Config):
    def __init__(self):
        Config.__init__(self)


class DevelopmentConfig(Config):
    def __init__(self):
        Config.__init__(self)

    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    ENV = 'test'
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
