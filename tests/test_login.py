
from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in page.url


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.open()

    login_page.login("standard_user", "wrong_password")

    expect(login_page.error_message).to_be_visible(timeout=5000)

    error = login_page.get_error_message()

    assert "Username and password do not match" in error
   