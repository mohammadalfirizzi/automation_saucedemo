class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def is_login_successful(self):
        return self.page.is_visible(".inventory_list")

    def get_error_message(self):
        return self.page.locator("h3[data-test='error']").inner_text()

    def is_error_visible(self):
        return self.page.is_visible("h3[data-test='error']")