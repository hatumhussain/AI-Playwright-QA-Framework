
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(page):

    # Login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product
    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    # Cart
    cart_page = CartPage(page)
    assert cart_page.get_item_count() == 1
    cart_page.checkout()

    # Checkout information
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_details(
        "Hatum", "Hussain", "98600"
    )

    # Finish order
    checkout_page.finish_order()

    # Verify confirmation
    assert checkout_page.get_confirmation() == "Thank you for your order!"