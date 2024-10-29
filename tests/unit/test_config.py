import os

basedir = os.path.abspath(os.path.dirname(__file__))

def test_development_config(app):
    app.config.from_object('config.DevelopmentConfig')
    assert app.config['DEBUG']
    assert not app.config['TESTING']
    # assert app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite:///" + os.path.join(basedir, "db.sqlite3")


def test_testing_config(app):
    app.config.from_object('config.TestingConfig')
    assert app.config['DEBUG']
    assert app.config['TESTING']
    # assert app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite:///" + os.path.join(basedir, "testdb.sqlite3")


def test_production_config(app):
    app.config.from_object('config.ProductionConfig')
    assert not app.config['DEBUG']
    assert not app.config['TESTING']
    # assert app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite:///" + os.path.join(basedir, "db.sqlite3")
