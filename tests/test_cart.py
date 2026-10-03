from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart_operations(page):

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(page)

    assert cart_page.get_item_count() == 1

    cart_page.remove_backpack()

    assert cart_page.get_item_count() == 0