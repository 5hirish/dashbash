import os


class Config:
    """Base configuration."""

    SECRET_KEY = '+7*o71ay6sk$w8g+w1+3sp0z89b(7@+@$_d3641y_skdvj_i1!'

    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13

    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    DB_DIALECT = 'postgresql'
    DB_DRIVER = 'psycopg2'
    DB_NAME = 'dashbash'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'

    DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar

    DB_USERNAME = 'felix'
    DB_PASSWORD = 'password'
    DB_HOSTNAME = 'localhost'
    DB_PORT = '5433'

    SQLALCHEMY_DATABASE_URI = Config.DB_DIALECT + '+' + Config.DB_DRIVER + '://' \
                              + DB_USERNAME + ':' + DB_PASSWORD +'@' + DB_HOSTNAME + ':' + DB_PORT + '/' + Config.DB_NAME


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_ENABLED = True

    DB_USERNAME = 'felix'
    DB_PASSWORD = 'password'
    DB_HOSTNAME = 'localhost'
    DB_PORT = '5433'

    SQLALCHEMY_DATABASE_URI = Config.DB_DIALECT + '+' + Config.DB_DRIVER + '://' \
                              + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOSTNAME + ':' + DB_PORT + '/' + Config.DB_NAME

    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'
    TESTING = True
    DEBUG = True

    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing

    DB_USERNAME = 'felix'
    DB_PASSWORD = 'password'
    DB_HOSTNAME = 'localhost'
    DB_PORT = '5433'

    SQLALCHEMY_DATABASE_URI = Config.DB_DIALECT + '+' + Config.DB_DRIVER + '://' \
                              + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOSTNAME + ':' + DB_PORT + '/' + Config.DB_NAME
