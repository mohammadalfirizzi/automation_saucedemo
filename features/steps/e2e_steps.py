from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given('user open saucedemo website')
def step_open(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()

@when('user login with "{username}" and "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)
    context.inventory_page = InventoryPage(context.page)

@then('user should be redirected to inventory page')
def step_login_success(context):
    assert context.login_page.is_login_successful()

@then('user should see login error message')
def step_login_error(context):
    assert context.login_page.is_error_visible()


@then('error message should contain "{expected_message}"')
def step_validate_error_message(context, expected_message):
    actual_message = context.login_page.get_error_message()
    assert expected_message in actual_message

@when('user add product to cart')
def step_add_product(context):
    context.inventory_page.add_first_product()

@when('user add product number {index}')
def step_add_product_index(context, index):
    context.inventory_page.add_product_by_index(int(index))


@when('user go to cart')
def step_go_cart(context):
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.page)


@when('user checkout with first name "{first}" last name "{last}" zip "{zip_code}"')
def step_checkout(context, first, last, zip_code):
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.page)

    clean_first = first.strip() 
    clean_last = last.strip()
    clean_zip = zip_code.strip()
    context.checkout_page.fill_information(clean_first, clean_last, clean_zip)
    
    context.checkout_page.finish_order()

@then('user should see order confirmation')
def step_verify(context):
    assert context.checkout_page.is_order_complete()


@then('all products should be displayed')
def step_products(context):
    assert context.inventory_page.is_product_list_visible()


@when('user sort products by "{option}"')
def step_sort(context, option):
    context.inventory_page.sort_products(option)


@then('products should be sorted correctly')
def step_sorted(context):
    items = context.page.locator(".inventory_item_name").all_inner_texts()
    assert items == sorted(items)


@when('user click first product')
def step_click_product(context):
    context.inventory_page.click_first_product()


@then('product detail page should be displayed')
def step_product_detail(context):
    assert context.inventory_page.is_product_detail_visible()

@then('cart badge should show "{count}"')
def step_cart_badge(context, count):
    badge = context.inventory_page.get_cart_badge()
    assert badge.inner_text() == count


@then('cart badge should be empty')
def step_cart_empty(context):
    assert context.inventory_page.get_cart_badge().count() == 0


@when('user remove product from cart')
def step_remove(context):
    context.inventory_page.remove_product()


@then('cart should display correct items')
def step_cart_items(context):
    assert len(context.cart_page.get_cart_items()) > 0

@then('user should see checkout error')
def step_checkout_error(context):
    is_error = context.checkout_page.is_error_visible()
    assert is_error, "Checkout error message NOT displayed"

@when('user click continue shopping')
def step_continue(context):
    context.cart_page.click_continue_shopping()


@when('user click logout')
def step_logout(context):
    context.inventory_page.click_menu()
    context.page.wait_for_timeout(1000)
    context.inventory_page.click_logout()


@then('user should be redirected to login page')
def step_login_page(context):
    assert context.page.is_visible("#login-button")

@then('cart should be empty')
def step_empty_cart(context):
    assert len(context.cart_page.get_cart_items()) == 0