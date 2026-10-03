from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.product_title = page.locator(".title")
        self.add_backpack_button = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.add_backpack_button.click()

    def open_cart(self):
        self.cart_link.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()