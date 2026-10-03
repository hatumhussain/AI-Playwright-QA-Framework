from playwright.sync_api import Page


def test_saucedemo_homepage(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.wait_for_timeout(7000)

    assert page.title() == "Swag Labs"