from decouple import config
import random
import os
import string

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv("SECRET_KEY", None)
    if not SECRET_KEY:
        SECRET_KEY = "".join(random.choice(string.ascii_lowercase) for i in range(32))

    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite3")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'db.sqlite3')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    # General Config
    # FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    # Assets Management
    ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")
    DATABASE = "sqlite:///db.sqlite3"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = DATABASE_URI + os.path.join(basedir, "testdb.sqlite3")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'testdb.sqlite3')}"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False
    
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


# Load all possible configurations
config_dict = {
    "Production": ProductionConfig,
    "Testing": TestingConfig,
    "Development" : DevelopmentConfig
}
