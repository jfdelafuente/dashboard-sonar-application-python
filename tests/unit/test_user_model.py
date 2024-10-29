from infocodest.models.users import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(username='admin',email='patkennedy79@gmail.com', password='FlaskIsAwesome')
    assert user.email == 'patkennedy79@gmail.com'
    assert user.__repr__() == '<users admin>'
    assert user.is_active
    assert not user.is_anonymous
    
    
def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
 
    assert new_user.email == 'admin@gmail.com'
    assert new_user.__repr__() == '<users admin>'
    assert new_user.is_active
    assert not new_user.is_anonymous
