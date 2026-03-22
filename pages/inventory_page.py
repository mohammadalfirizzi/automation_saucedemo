class InventoryPage:
    def __init__(self, page):
        self.page = page

    def get_products(self):
        return self.page.locator(".inventory_item").all()

    def is_product_list_visible(self):
        return len(self.get_products()) > 0

    def sort_products(self, option):
        self.page.select_option(".product_sort_container", option)

    def remove_product(self):
        self.page.wait_for_selector(".inventory_item")
        self.page.locator(".inventory_item").first.locator("button").click()

    def get_cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")

    def click_first_product(self):
        self.page.click(".inventory_item_name")

    def is_product_detail_visible(self):
        return self.page.is_visible(".inventory_details_name")

    def click_menu(self):
        self.page.click("#react-burger-menu-btn")

    def click_logout(self):
        self.page.click("#logout_sidebar_link")

    def wait_for_page_loaded(self):
        self.page.wait_for_selector(".inventory_item")

    def get_products(self):
        self.wait_for_page_loaded()
        return self.page.locator(".inventory_item").all()

    def is_product_list_visible(self):
        self.wait_for_page_loaded()
        return len(self.get_products()) > 0

    def add_first_product(self):
        self.wait_for_page_loaded()

        button = self.page.locator(".inventory_item button").first
        text = button.inner_text()

        if text == "Add to cart":
            button.click()

    def add_product_by_index(self, index):
        self.wait_for_page_loaded()

        button = self.page.locator(".inventory_item button").nth(index)
        text = button.inner_text()

        if text == "Add to cart":
            button.click()
        