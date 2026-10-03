from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_product_to_cart(page):

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)

    assert products_page.product_title.inner_text() == "Products"

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"