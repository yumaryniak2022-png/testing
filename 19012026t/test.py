from main import login

def test_login_success():
    assert login("admin", "admin123") is True

def test_login_fail():
    assert login("admin", "1234") is False
