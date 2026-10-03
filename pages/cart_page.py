from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_item = page.locator(".cart_item")
        self.remove_backpack_button = page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        )
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_item_count(self):
        return self.cart_item.count()

    def remove_backpack(self):
        self.remove_backpack_button.click()

    def checkout(self):
        self.checkout_button.click()