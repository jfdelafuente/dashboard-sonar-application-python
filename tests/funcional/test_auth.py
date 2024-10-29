def test_main_route_requires_login(test_client):
    # Ensure main route requres logged in user.
    response = test_client.get("/", follow_redirects=True)
    assert response.status_code == 200
    assert b"INFOCODE - Login | Orange" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    
def test_logout_route_requires_login(test_client):
    # Ensure logout route requres logged in user.
    response = test_client.get("/logout", follow_redirects=True)
    assert b"INFOCODE - Login | Orange" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data


def test_correct_login(test_client, init_database):
    # Ensure login behaves correctly with correct credentials
    response = test_client.post(
            "/login",
            data=dict(username="admin_user", password="admin_user"),
            follow_redirects=True,
    )
    # assert (current_user.email == "ad@min.com")
    # self.assertTrue(current_user.is_active)
    # self.assertTrue(response.status_code == 200)
    assert response.status_code == 200
    # assert b'Name: Alice' in response.data
    # assert b'Age: 25' in response.data

def test_logout_behaves_correctly(test_client):
    # Ensure logout behaves correctly, regarding the session
    test_client.post(
                "/login",
                data=dict(username="admin_user", password="admin_user"),
                follow_redirects=True,
    )
    response = test_client.get("/logout", follow_redirects=True)
    # self.assertIn(b"You were logged out.", response.data)
    # self.assertFalse(current_user.is_active)


# def test_home_auth(test_client):
#     response = test_client.get("/")
#     # Check that there was one redirect response.
#     # assert len(response.history) == 1
#     # Check that the second request was to the index page.
#     assert response.request.path == "/login"


def test_login_page(test_client):
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"INFOCODE - Login | Orange" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data


def test_register_page(test_client):
    response = test_client.get("/register")
    assert response.status_code == 200
    assert b"INFOCODE - Register | Orange" in response.data
    assert b"Username" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_correct_register(test_client):
    with test_client:
        response = test_client.post(
            "/register",
            data=dict(username="admin_user", email="admin@example.com", password="admin_user", confirm_password="admin_user"),
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert b"Account created successfully" in response.data


def test_password_page(test_client):
    response = test_client.get("/password")
    assert response.status_code == 200
    assert b"INFOCODE - Password Recovery | Orange" in response.data


# def test_logout_redirect(test_client):
#     response = test_client.get("/logout")
#     # Check that there was one redirect response.
#     # assert len(response.history) == 1
#     # Check that the second request was to the index page.
#     assert response.request.path == "/login"
