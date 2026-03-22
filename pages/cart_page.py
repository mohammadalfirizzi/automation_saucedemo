class CartPage:
    def __init__(self, page):
        self.page = page

    def get_cart_items(self):
        return self.page.locator(".cart_item").all()

    def click_checkout(self):
        self.page.click("#checkout")

    def click_continue_shopping(self):
        self.page.click("#continue-shopping")