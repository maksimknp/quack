DB_NAME = 'quackdb'
DB_HOST = 'localhost'
DB_USER = 'quack'
DB_PASS = 'quack'

JSONRPC_URL = '/api/'


class ProductionConfig(object):
    pass


class TestConfig(object):
    TESTING = True
    DEBUG = True
