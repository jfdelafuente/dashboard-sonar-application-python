import pytest
import os
from infocodest import create_app
from infocodest.extensions import db
from config import config_dict
from infocodest.models.users import User

@pytest.fixture()
def app():
    get_config_mode = 'Testing'
    app_config = config_dict[get_config_mode.capitalize()]
    app = create_app(app_config)
    # other setup can go here
    yield app
    # clean up / reset resources here


# @pytest.fixture()
# def test_client(app):
#         with app.test_client() as client:
#             return client
        


@pytest.fixture(scope='module')
def new_user():
    user = User(username='admin_user',email='admin@gmail.com', password='admin_user')
    return user


@pytest.fixture()
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    get_config_mode = 'Testing'
    app_config = config_dict[get_config_mode.capitalize()]
    flask_app = create_app(app_config)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client



@pytest.fixture()
def runner(app):
    return app.test_cli_runner()



@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    default_user = User(username='admin_user',email='admin@gmail.com', password='admin_user')
    db.session.add(default_user)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    # db.drop_all()
