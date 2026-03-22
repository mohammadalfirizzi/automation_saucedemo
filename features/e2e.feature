Feature: Product, Cart, Checkout, Navigation, Logout End to End

  Background:
    Given user open saucedemo website
    When user login with "standard_user" and "secret_sauce"
    Then user should be redirected to inventory page

  Scenario: View product list
    Then all products should be displayed

  Scenario: Sort products A-Z
    When user sort products by "az"
    Then products should be sorted correctly

  Scenario: View product detail
    When user click first product
    Then product detail page should be displayed

  Scenario: Add item to cart
    When user add product to cart
    Then cart badge should show "1"

  Scenario: Remove item from cart
    When user remove product from cart
    Then cart badge should be empty

  Scenario: Add same item multiple times
    When user add product number 0
    And user add product number 1
    Then cart badge should show "2"

  Scenario: View cart page
    When user add product to cart
    And user go to cart
    Then cart should display correct items

  Scenario: Complete purchase
    When user add product to cart
    And user go to cart
    And user checkout with first name "John" last name "Doe" zip "12345"
    Then user should see order confirmation

  Scenario: Empty first name
    When user add product to cart
    And user go to cart
    When user checkout with first name " " last name "Doe" zip "12345"
    Then user should see checkout error

  Scenario: Empty last name
    When user add product to cart
    And user go to cart
    And user checkout with first name "John" last name " " zip "12345"
    Then user should see checkout error

  Scenario: Empty postal code
    When user add product to cart
    And user go to cart
    And user checkout with first name "John" last name "Doe" zip " "
    Then user should see checkout error

  Scenario: Continue shopping
    When user add product to cart
    And user go to cart
    And user click continue shopping
    Then user should be redirected to inventory page

  Scenario: Logout successfully
    When user click logout
    Then user should be redirected to login page