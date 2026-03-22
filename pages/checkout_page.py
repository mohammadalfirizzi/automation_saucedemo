class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_information(self, first, last, zip_code):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip_code)
        self.page.wait_for_timeout(1000)
        self.page.click("#continue")

    def finish_order(self):
        if self.page.is_visible("#finish"):
            self.page.click("#finish")

    def is_order_complete(self):
        return self.page.is_visible(".complete-header")

    def is_error_visible(self):
        return self.page.is_visible("h3[data-test='error']")